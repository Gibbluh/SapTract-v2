const mongoose = require("mongoose");

mongoose.set('bufferCommands', false); // CRITICAL: fail fast, don't hang

const connectDB = async () => {
    try {
        const uri = process.env.MONGO_URI;
        if (!uri) {
            console.warn("[AI Studio] MONGO_URI not configured — running with database offline");
            return;
        }
        await mongoose.connect(uri, { serverSelectionTimeoutMS: 4000 });
        console.log("MongoDB connected successfully");
    } catch (error) {
        console.warn("[AI Studio] MongoDB connection error:", error.message);
        console.warn("[AI Studio] Continuing with database offline; safe fallbacks active");
    }
};

module.exports = connectDB;