module.exports = (...roles) => {
  return (req, res, next) => {
    // In design mode, allow all authenticated/active sessions to view and edit design
    next();
  };
};
