const jwt = require('jsonwebtoken');
const { resolveUserId } = require('../utils/resolveUserId');

const JWT_SECRET = process.env.TOKEN || process.env.JWT_SECRET || 'saptrac_design_secret_2026';
const JWT_EXPIRES = '7d';

const generateToken = (user) => {
  return jwt.sign(
    { id: user._id, email: user.email, role: user.role, fullName: user.fullName },
    JWT_SECRET,
    { expiresIn: JWT_EXPIRES }
  );
};

exports.registerUser = async (req, res) => {
  const { fullName, email } = req.body || {};
  const resolvedId = await resolveUserId({ role: 'Super Admin', email });
  const mockUser = {
    _id: resolvedId,
    fullName: fullName || 'Demo User',
    email: email || 'admin@saptrac.com',
    role: 'Super Admin',
    isActive: true,
  };
  const token = generateToken(mockUser);
  return res.status(201).json({ user: mockUser, token });
};

exports.loginUser = async (req, res) => {
  try {
    const { email, password } = req.body || {};
    const em = (email || '').trim().toLowerCase();

    let role = 'Super Admin';
    let name = 'Super Administrator';

    if (em.includes('driver')) {
      role = 'Driver';
      name = 'Fleet Driver';
    } else if (em.includes('mechanic') || em.includes('mech')) {
      role = 'Mechanic';
      name = 'Chief Mechanic';
    } else if (em.includes('staff')) {
      role = 'Operational Manager';
      name = 'Operations Staff';
    } else if (em.includes('cashier')) {
      role = 'Cashier';
      name = 'Remittance Cashier';
    } else {
      role = 'Super Admin';
      name = 'Super Administrator';
    }

    const resolvedId = await resolveUserId({ role, email });

    // Pure design mode: ANY credentials succeed instantly
    const user = {
      _id: resolvedId,
      fullName: name,
      email: email || `${role.toLowerCase().replace(/\s+/g, '')}@saptrac.com`,
      role: role,
      isActive: true,
      contactNumber: '09123456789',
    };

    const token = generateToken(user);
    return res.status(200).json({
      success: true,
      message: 'Login successful (Design Mode)',
      user,
      token,
    });
  } catch (err) {
    console.error('Design mode login error:', err);
    const resolvedId = await resolveUserId({ role: 'Super Admin' });
    const user = {
      _id: resolvedId,
      fullName: 'Super Administrator',
      email: 'admin@saptrac.com',
      role: 'Super Admin',
      isActive: true,
    };
    return res.status(200).json({
      success: true,
      user,
      token: generateToken(user),
    });
  }
};

exports.getCurrentUser = async (req, res) => {
  const role = req.user?.role || 'Super Admin';
  const resolvedId = await resolveUserId(req.user);
  return res.json({
    user: {
      _id: resolvedId,
      fullName: req.user?.fullName || (role === 'Driver' ? 'Fleet Driver' : role === 'Mechanic' ? 'Chief Mechanic' : 'Super Administrator'),
      email: req.user?.email || 'admin@saptrac.com',
      role: role,
      isActive: true,
      contactNumber: '09123456789',
    },
  });
};

exports.logoutUser = async (req, res) => {
  return res.json({ message: 'Logged out successfully.' });
};
