// Centralized error handler middleware for Express
const mongoose = require('mongoose');

function errorHandler(err, req, res, next) {

  // Centralized error handler middleware for Express
  console.error("=== ERROR HANDLER ===");
  console.error(err);

  // Mongoose offline / disconnected / buffer commands error
  if (
    err.name === 'MongooseError' ||
    err.name === 'MongoNetworkError' ||
    err.name === 'MongoServerSelectionError' ||
    (err.message && (err.message.includes('buffering timed out') || err.message.includes('bufferCommands')))
  ) {
    console.warn('[AI Studio] Database offline — returning fallback response for path:', req.path);
    if (req.method === 'GET') {
      return res.json({ success: true, data: [], items: [], units: [], drivers: [], schedules: [], total: 0, count: 0 });
    }
    return res.status(503).json({
      success: false,
      message: 'Service temporarily unavailable (database offline). To connect a live database, set MONGO_URI in Settings.'
    });
  }

  let statusCode = err.status || 500;
  let message = err.message || "Internal Server Error";
  let errors = null;

  // Mongoose validation error
  if (err instanceof mongoose.Error.ValidationError) {
    statusCode = 400;
    message = 'Validation error';
    errors = Object.values(err.errors).map(e => e.message);
  }

  // Mongoose bad ObjectId
  if (err instanceof mongoose.Error.CastError) {
    statusCode = 400;
    message = `Invalid ${err.path}: ${err.value}`;
  }

  // Duplicate key error (MongoServerError)
  if (err.code && err.code === 11000) {
    statusCode = 409;
    const field = Object.keys(err.keyValue)[0];
    message = `Duplicate value for field: ${field}`;
  }

  // Express-validator errors (from validation middleware)
  if (err.errors && Array.isArray(err.errors)) {
    statusCode = 400;
    message = 'Validation error';
    errors = err.errors.map(e => e.msg || e.message);
  }

  // Hide stack/message in production
  if (process.env.NODE_ENV === 'production' && statusCode === 500) {
    message = 'Something went wrong.';
  }

  res.status(statusCode).json({
    success: false,
    message,
    ...(errors && { errors }),
  });
}

module.exports = errorHandler;
