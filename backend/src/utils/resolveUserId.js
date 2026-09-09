const mongoose = require('mongoose');
const User = require('../models/User');

/**
 * Resolves a valid MongoDB ObjectId for a user reference.
 * Handles cases where user.id is a string like "user_Super Admin" or an invalid ObjectId.
 */
async function resolveUserId(userOrId, preferredRole = 'Super Admin') {
  if (!userOrId) {
    try {
      const defaultUser = await User.findOne({
        $or: [{ role: 'Super Admin' }, { role: 'Administrator' }]
      });
      if (defaultUser?._id) return defaultUser._id;
    } catch (_) {}
    return new mongoose.Types.ObjectId();
  }

  const rawId = typeof userOrId === 'object' && userOrId !== null
    ? (userOrId.id || userOrId._id)
    : userOrId;

  if (rawId && mongoose.Types.ObjectId.isValid(rawId)) {
    return new mongoose.Types.ObjectId(rawId);
  }

  const role = (typeof userOrId === 'object' && userOrId?.role) || preferredRole;
  const email = typeof userOrId === 'object' && userOrId?.email;

  try {
    const candidates = [];
    if (email) candidates.push({ email });
    if (role) {
      candidates.push({ role });
      // Also handle case matching
      if (role.toLowerCase().includes('admin')) {
        candidates.push({ role: 'Super Admin' });
        candidates.push({ role: 'Administrator' });
      }
    }
    candidates.push({ role: 'Super Admin' });
    candidates.push({ role: 'Administrator' });

    const matchedUser = await User.findOne({ $or: candidates });
    if (matchedUser && matchedUser._id) {
      return matchedUser._id;
    }

    const anyUser = await User.findOne({});
    if (anyUser && anyUser._id) {
      return anyUser._id;
    }
  } catch (err) {
    console.warn('[resolveUserId] Database lookup error:', err.message);
  }

  // Fallback to a valid newly generated ObjectId so database operations never crash
  return new mongoose.Types.ObjectId();
}

module.exports = { resolveUserId };
