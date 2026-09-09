const scheduleService = require('../services/schedule.service');
const { resolveUserId } = require('../utils/resolveUserId');

// Create Schedule
exports.createSchedule = async (req, res, next) => {
  try {
    const assignedBy = await resolveUserId(req.user);
    const schedule = await scheduleService.createScheduleService(
      {
        ...req.body,
        assignedBy,
      },
      assignedBy
    );
    res.status(201).json({ schedule });
  } catch (err) {
    next(err);
  }
};

// Get Schedules (list, pagination, filter, sort)
exports.getSchedules = async (req, res, next) => {
  try {
    const result = await scheduleService.getSchedulesService(req.query);
    res.json(result);
  } catch (err) {
    next(err);
  }
};

// Get Single Schedule
exports.getSingleSchedule = async (req, res, next) => {
  try {
    const schedule = await scheduleService.getSingleScheduleService(req.params.id);
    res.json({ schedule });
  } catch (err) {
    next(err);
  }
};

// Update Schedule
exports.updateSchedule = async (req, res, next) => {
  try {
    const performedBy = await resolveUserId(req.user);
    const schedule = await scheduleService.updateScheduleService(req.params.id, req.body, performedBy);
    res.json({ schedule });
  } catch (err) {
    next(err);
  }
};

// Delete Schedule (soft delete)
exports.deleteSchedule = async (req, res, next) => {
  try {
    await scheduleService.deleteScheduleService(req.params.id);
    res.json({ message: 'Schedule deleted successfully.' });
  } catch (err) {
    next(err);
  }
};

// Swap Schedules (switch drivers between two schedules)
exports.swapSchedules = async (req, res, next) => {
  try {
    const { scheduleAId, scheduleBId } = req.body;
    if (!scheduleAId || !scheduleBId) {
      return res.status(400).json({ message: 'Both scheduleAId and scheduleBId are required for switching shifts.' });
    }
    const performedBy = await resolveUserId(req.user);
    const result = await scheduleService.swapSchedulesService(scheduleAId, scheduleBId, performedBy);
    res.json(result);
  } catch (err) {
    next(err);
  }
};

