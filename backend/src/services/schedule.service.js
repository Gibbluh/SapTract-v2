const Schedule = require('../models/schedule.model');
const ScheduleHistory = require('../models/scheduleHistory.model');
const mongoose = require('mongoose');
const Driver = require('../models/driver.model');
const Unit = require('../models/unit.model');
const User = require('../models/User');
const { emitScheduleEvent } = require('../socket/socket');
const { createNotification } = require('./notification.service');
const { sendSMS } = require('./sms.service');
const { resolveUserId } = require('../utils/resolveUserId');

async function getDriverNotificationData(driverId) {
  const driver = await Driver.findById(driverId);

  if (!driver) {
    throw new Error('Driver not found.');
  }

  const user = await User.findOne({
    email: driver.email,
  });

  return {
    driver,
    user,
  };
}

async function getUnitDisplayName(unitId) {
  const unit = await Unit.findById(unitId);

  return (
    unit?.plateNumber ||
    unit?.bodyNumber ||
    'Assigned Unit'
  );
}

function formatScheduleDate(date) {
  return new Date(date)
    .toISOString()
    .slice(0, 10);
}

async function notifyDriverScheduleAssigned(schedule) {
  const { driver, user } = await getDriverNotificationData(
    schedule.driver
  );

  const unitName = await getUnitDisplayName(schedule.unit);
  const formattedDate = formatScheduleDate(schedule.shiftDate);

  // In-app notification
  if (user) {
    await createNotification({
      recipient: user._id,
      title: 'New Schedule Assigned',
      message:
        `You have been assigned a schedule on ${formattedDate} ` +
        `for ${schedule.shiftType}.`,
      type: 'ScheduleAssigned',
    });
  }

  // SMS
  const smsMessage =
    `SAPTRAC: Hi ${driver.firstName} ${driver.lastName}, ` +
    `you are scheduled on ${formattedDate}, ${schedule.shiftType}. ` +
    `Unit: ${unitName}. Route: ${schedule.route}.`;

  try {
    const response = await sendSMS({
      number: driver.phone,
      message: smsMessage,
    });

    console.log(
      `Schedule SMS sent successfully to ${driver.phone}`,
      response
    );
  } catch (error) {
    console.error(
      'Schedule created but SMS failed:',
      error.response?.data || error.message
    );
  }
}

async function notifyDriverScheduleCancelled(schedule) {
  const { driver, user } =
    await getDriverNotificationData(schedule.driver);

  const formattedDate = formatScheduleDate(
    schedule.shiftDate
  );

  // In-app notification
  if (user) {
    await createNotification({
      recipient: user._id,
      title: 'Schedule Cancelled',
      message:
        `Your schedule on ${formattedDate} has been cancelled.`,
      type: 'ScheduleCancelled',
    });
  }

  // SMS
  const smsMessage =
    `SAPTRAC: Hi ${driver.firstName} ${driver.lastName}, ` +
    `your schedule on ${formattedDate}, ` +
    `${schedule.shiftType}, has been cancelled.`;

  try {
    const response = await sendSMS({
      number: driver.phone,
      message: smsMessage,
    });

    console.log(
      `Cancellation SMS sent successfully to ${driver.phone}`,
      response
    );
  } catch (error) {
    console.error(
      'Cancellation SMS failed:',
      error.response?.data || error.message
    );
  }
}

// Helper: Build query for filtering
function buildScheduleQuery({ status, date, driver, unit, scheduleType, conflictDetected }) {
  const query = { deletedAt: null };
  if (status) query.status = status;
  if (date) query.shiftDate = date;
  if (driver) query.driver = driver;
  if (unit) query.unit = unit;
  if (scheduleType) query.scheduleType = scheduleType;
  if (typeof conflictDetected === 'boolean') query.conflictDetected = conflictDetected;
  return query;
}

// Helper: Check for overlapping schedules
async function hasScheduleConflict({ driver, unit, shiftDate, shiftStart, shiftEnd, excludeId = null }) {
  const conflictQuery = {
    deletedAt: null,
    shiftDate,
    $or: [
      { driver },
      { unit },
    ],
    status: { $in: ['Scheduled', 'Active'] },
    $expr: {
      $and: [
        { $lt: [ '$shiftStart', shiftEnd ] },
        { $gt: [ '$shiftEnd', shiftStart ] },
      ],
    },
  };
  if (excludeId) {
    if (Array.isArray(excludeId)) {
      conflictQuery._id = { $nin: excludeId };
    } else {
      conflictQuery._id = { $ne: excludeId };
    }
  }
  const conflict = await Schedule.findOne(conflictQuery);
  return !!conflict;
}

// Helper: Log schedule history (scalable, audit-trail)
async function logScheduleHistory({ schedule, actionType, performedBy, previousData, newData }) {
  try {
    const validPerformedBy = await resolveUserId(performedBy);
    await ScheduleHistory.create({
      schedule: schedule._id || schedule,
      actionType,
      performedBy: validPerformedBy,
      previousData,
      newData,
    });
  } catch (err) {
    // Optionally log error, but do not block main flow
    console.error('Failed to log schedule history:', err);
  }
}

// Create Schedule
async function createScheduleService(data, performedBy) {
  const { driver, unit, shiftDate, shiftStart, shiftEnd } = data;
  if (!driver || !unit || !shiftDate || !shiftStart || !shiftEnd) {
    throw new Error('Missing required schedule fields.');
  }

  const validAssignedBy = await resolveUserId(data.assignedBy || performedBy);
  const validPerformedBy = await resolveUserId(performedBy || data.assignedBy);
  data.assignedBy = validAssignedBy;

  // Check for conflicts
  const conflict = await hasScheduleConflict({ driver, unit, shiftDate, shiftStart, shiftEnd });
  if (conflict) {
    // Notify assignedBy (performedBy) about conflict
    if (validPerformedBy) {
      await createNotification({
        recipient: validPerformedBy,
        title: 'Schedule Conflict Detected',
        message: 'A schedule conflict was detected for the selected driver or unit.',
        type: 'ConflictDetected',
      });
    }
    throw new Error('Schedule conflict detected: driver or unit already assigned at this time.');
  }
  // Create schedule
  const schedule = new Schedule(data);
  await schedule.save();
  emitScheduleEvent('scheduleCreated', schedule);
  // Log history
  await logScheduleHistory({
    schedule,
    actionType: 'Created',
    performedBy: validPerformedBy,
    previousData: null,
    newData: schedule.toObject(),
  });
  // Notify driver asynchronously so assignment returns promptly
  notifyDriverScheduleAssigned(schedule).catch(err => {
    console.error('Failed to notify driver of assignment:', err?.message || err);
  });
  return schedule;
}

// Get Schedules (pagination, filter, sort)
async function getSchedulesService({ page = 1, limit = 10, ...filters }) {
  page = parseInt(page);
  limit = parseInt(limit);
  const query = buildScheduleQuery(filters);
  const sort = { createdAt: -1 };
  const total = await Schedule.countDocuments(query);
  const schedules = await Schedule.find(query)
  .sort(sort)
  .skip((page - 1) * limit)
  .limit(limit)
  .populate('driver')
  .populate('unit');
  return {
    schedules,
    total,
    page,
    totalPages: Math.ceil(total / limit),
  };
}

// Get Single Schedule
async function getSingleScheduleService(id) {
  if (!mongoose.Types.ObjectId.isValid(id)) throw new Error('Invalid schedule ID.');
  const schedule = await Schedule.findOne({ _id: id, deletedAt: null })
    .populate('driver unit assignedBy');
  if (!schedule) throw new Error('Schedule not found.');
  return schedule;
}

// Update Schedule
async function updateScheduleService(id, data, performedBy) {
  if (!mongoose.Types.ObjectId.isValid(id)) throw new Error('Invalid schedule ID.');
  const schedule = await Schedule.findOne({ _id: id, deletedAt: null });
  if (!schedule) throw new Error('Schedule not found.');

  if (data.assignedBy) {
    data.assignedBy = await resolveUserId(data.assignedBy);
  }
  const validPerformedBy = await resolveUserId(performedBy);

  // If updating driver/unit/time, check for conflicts
  const updateFields = ['driver', 'unit', 'shiftDate', 'shiftStart', 'shiftEnd'];
  const needsConflictCheck = updateFields.some(f => data[f] && data[f] !== schedule[f]);
  if (needsConflictCheck) {
    const conflict = await hasScheduleConflict({
      driver: data.driver || schedule.driver,
      unit: data.unit || schedule.unit,
      shiftDate: data.shiftDate || schedule.shiftDate,
      shiftStart: data.shiftStart || schedule.shiftStart,
      shiftEnd: data.shiftEnd || schedule.shiftEnd,
      excludeId: id,
    });
    if (conflict) throw new Error('Schedule conflict detected: driver or unit already assigned at this time.');
  }
  const previousData = schedule.toObject();
  Object.assign(schedule, data);
  await schedule.save();
  emitScheduleEvent('scheduleUpdated', schedule);
  // Log history
  await logScheduleHistory({
    schedule,
    actionType: 'Updated',
    performedBy: validPerformedBy,
    previousData,
    newData: schedule.toObject(),
  });
  // If status changed to Cancelled, notify driver asynchronously
  if (data.status === 'Cancelled') {
    notifyDriverScheduleCancelled(schedule).catch(err => {
      console.error('Failed to notify driver of cancellation:', err?.message || err);
    });
  }

  return schedule;
}

// Soft Delete Schedule
async function deleteScheduleService(id, performedBy) {
  if (!mongoose.Types.ObjectId.isValid(id)) throw new Error('Invalid schedule ID.');
  const schedule = await Schedule.findOne({ _id: id, deletedAt: null });
  if (!schedule) throw new Error('Schedule not found.');
  const previousData = schedule.toObject();
  schedule.deletedAt = new Date();
  await schedule.save();
  emitScheduleEvent('scheduleDeleted', { _id: schedule._id });
  // Log history
  await logScheduleHistory({
    schedule,
    actionType: 'Deleted',
    performedBy,
    previousData,
    newData: schedule.toObject(),
  });
  await notifyDriverScheduleCancelled(schedule);

return {
  message: 'Schedule deleted (soft delete).',
};
}

// Swap Schedules (switch drivers between two schedules)
async function swapSchedulesService(scheduleAId, scheduleBId, performedBy) {
  if (!mongoose.Types.ObjectId.isValid(scheduleAId) || !mongoose.Types.ObjectId.isValid(scheduleBId)) {
    throw new Error('Invalid schedule ID(s).');
  }

  const scheduleA = await Schedule.findOne({ _id: scheduleAId, deletedAt: null });
  const scheduleB = await Schedule.findOne({ _id: scheduleBId, deletedAt: null });

  if (!scheduleA || !scheduleB) {
    throw new Error('One or both schedules not found.');
  }

  const validPerformedBy = await resolveUserId(performedBy);

  const driverA = scheduleA.driver;
  const driverB = scheduleB.driver;

  const prevA = scheduleA.toObject();
  const prevB = scheduleB.toObject();

  scheduleA.driver = driverB;
  scheduleB.driver = driverA;

  await scheduleA.save();
  await scheduleB.save();

  const populatedA = await Schedule.findById(scheduleA._id).populate('driver unit assignedBy');
  const populatedB = await Schedule.findById(scheduleB._id).populate('driver unit assignedBy');

  emitScheduleEvent('scheduleUpdated', populatedA);
  emitScheduleEvent('scheduleUpdated', populatedB);

  await logScheduleHistory({
    schedule: scheduleA,
    actionType: 'Updated',
    performedBy: validPerformedBy,
    previousData: prevA,
    newData: scheduleA.toObject(),
  });

  await logScheduleHistory({
    schedule: scheduleB,
    actionType: 'Updated',
    performedBy: validPerformedBy,
    previousData: prevB,
    newData: scheduleB.toObject(),
  });

  return {
    scheduleA: populatedA,
    scheduleB: populatedB,
  };
}

// Status Change (utility for audit trail)
async function logStatusChange(schedule, oldStatus, newStatus, performedBy) {
  if (oldStatus !== newStatus) {
    await logScheduleHistory({
      schedule,
      actionType: 'StatusChanged',
      performedBy,
      previousData: { status: oldStatus },
      newData: { status: newStatus },
    });
  }
}

module.exports = {
  createScheduleService,
  getSchedulesService,
  getSingleScheduleService,
  updateScheduleService,
  deleteScheduleService,
  swapSchedulesService,
  logStatusChange,
};