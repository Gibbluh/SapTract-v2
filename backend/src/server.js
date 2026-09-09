require("dotenv").config({
  path: require("path").resolve(__dirname, "../.env"),
});

const userRoutes = require("./routes/userRoutes");
const driverRoutes = require("./routes/driver.routes");
const unitRoutes = require("./routes/unit.routes");
const scheduleRoutes = require("./routes/schedule.routes");
const fuelRoutes = require("./routes/fuel.routes");
const remittanceRoutes = require("./routes/remittance.routes");
const maintenanceRoutes = require("./routes/maintenance.routes");
const analyticsRoutes = require("./routes/analytics.routes");
const repairHistoryRoutes = require("./routes/repairHistory.routes");

const revenueRoutes = require("./routes/revenueRoutes");
const express = require("express");
const cors = require("cors");
const http = require("http");
const fs = require("fs");

const notesRoutes = require("./routes/notesRoutes");
const authRoutes = require("./routes/authRoutes");
const connectDB = require("./config/db.js");
const path = require("path");
const rateLimiterFactory = require("./middleware/rateLimiter");
const { createRatelimit } = require('./config/upstash');
const errorHandler = require("./middleware/errorHandler");
const { initSocket } = require("./socket/socket");

// Create a stricter limiter for dashboard endpoints (to prevent dashboard spamming)
const dashboardLimiter = rateLimiterFactory.withLimiter(createRatelimit(20, '1 m'), { allowAnalyticsPoll: true });

// Global default limiter (applied after socket and public paths are allowed)
const globalLimiter = rateLimiterFactory.default;

process.on('uncaughtException', (err) => {
  console.error('[Process] Uncaught exception:', err);
});
process.on('unhandledRejection', (reason) => {
  console.error('[Process] Unhandled promise rejection:', reason);
});

const app = express();
const PORT = 3000;
const HOST = "0.0.0.0";
// Apply middleware order carefully: socket and health/public routes first, then rate limiter for others
app.use(cors({
    origin: (origin, callback) => callback(null, true),
    credentials: true,
}));
app.use(express.json()); // Middleware to parse JSON request bodies

// Public or health routes that should not be rate-limited
app.get(['/health', '/api/health', '/healthz'], (req, res) => res.json({ status: 'healthy', uptime: process.uptime() }));

// Mount socket.io path before global limit to avoid blocking handshake
app.use('/socket.io', (req, res, next) => next());

app.use("/api/users", userRoutes);
app.use("/api/drivers", driverRoutes);
app.use("/api/units", unitRoutes);
app.use("/api/schedules", scheduleRoutes);
app.use("/api/fuel", fuelRoutes);
app.use("/api/remittances", remittanceRoutes);
app.use("/api/maintenance", maintenanceRoutes);
app.use("/api/analytics", analyticsRoutes);
app.use("/api/repair-history", repairHistoryRoutes);

app.use("/api/notes", notesRoutes);
app.use("/api/auth", authRoutes);
app.use("/api/revenue", revenueRoutes);

// Serve frontend static files from dist
const candidateDistPaths = [
  path.resolve(__dirname, "../../frontend/dist"),
  path.resolve(__dirname, "../../dist"),
  path.resolve(__dirname, "../dist"),
  path.resolve(process.cwd(), "frontend/dist"),
  path.resolve(process.cwd(), "dist")
];
const distPath = candidateDistPaths.find(p => fs.existsSync(path.join(p, "index.html"))) || candidateDistPaths[0];

if (fs.existsSync(distPath)) {
  app.use(express.static(distPath));
}

// Fallback to index.html for SPA routes
app.use((req, res, next) => {
  if (req.method !== 'GET') return next();
  if (req.path.startsWith("/api") || req.path.startsWith("/socket.io") || req.path.startsWith("/health")) {
    return next();
  }
  const indexPath = path.join(distPath, "index.html");
  if (fs.existsSync(indexPath)) {
    return res.sendFile(indexPath);
  }
  next();
});

app.use(errorHandler);

const server = http.createServer(app);
const io = initSocket(server);

// Always bind to PORT (3000) immediately
server.listen(PORT, HOST, () => {
  console.log(`Server is running on ${HOST}:${PORT}`);
});

// Also bind to Cloud Run's process.env.PORT if provided and different from 3000
const targetPort = process.env.PORT ? parseInt(process.env.PORT, 10) : null;
if (targetPort && targetPort !== PORT) {
  const prodServer = http.createServer(app);
  if (io && typeof io.attach === 'function') {
    try { io.attach(prodServer); } catch (_) {}
  }
  prodServer.listen(targetPort, HOST, () => {
    console.log(`Production listener active on ${HOST}:${targetPort}`);
  }).on('error', (err) => {
    console.log(`Port ${targetPort} notice: ${err.message}`);
  });
}

// Initialize database in background without stalling HTTP server startup probes
connectDB().catch(err => {
  console.warn("MongoDB startup warning:", err?.message || err);
});
