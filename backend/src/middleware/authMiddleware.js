const jwt = require("jsonwebtoken");
const User = require("../models/User");
const { resolveUserId } = require("../utils/resolveUserId");

const authenticate = async (req, res, next) => {
  try {
    const authHeader = req.headers.authorization;
    if (!authHeader || !authHeader.startsWith("Bearer ")) {
      return res.status(401).json({ message: "Missing token" });
    }

    const token = authHeader.split(" ")[1];
    const secret = process.env.TOKEN || process.env.JWT_SECRET || "saptrac_dev_secret_key_2026";

    const payload = jwt.verify(token, secret);
    // attach user details and ensure id is a valid Mongo ObjectId
    const resolvedId = await resolveUserId(payload);
    req.user = {
      ...payload,
      id: resolvedId,
      _id: resolvedId,
    };

    return next();
  } catch (err) {
    return res.status(401).json({ message: "Invalid token" });
  }
};

const authorizeRoles = (allowedRoles = []) => {
  return (req, res, next) => {
    if (!req.user) return res.status(401).json({ message: "Not authenticated" });
    if (!allowedRoles.length) return next();

    if (!allowedRoles.includes(req.user.role)) {
      return res.status(403).json({ message: "Forbidden: Insufficient role" });
    }

    return next();
  };
};

module.exports = { authenticate, authorizeRoles };
