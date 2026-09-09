exports.register = (req, res, next) => {
  next();
};

exports.login = (req, res, next) => {
  // Never block in design mode
  next();
};
