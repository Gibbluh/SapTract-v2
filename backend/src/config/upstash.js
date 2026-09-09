const { Ratelimit } = require('@upstash/ratelimit');
const { Redis } = require('@upstash/redis');
const dotenv = require("dotenv");   
dotenv.config();    

let redis;
let defaultLimiter;

try {
  if (process.env.UPSTASH_REDIS_REST_URL && process.env.UPSTASH_REDIS_REST_TOKEN) {
    redis = Redis.fromEnv();
    defaultLimiter = new Ratelimit({
      redis,
      limiter: Ratelimit.slidingWindow(100, '1 m'),
      analytics: true,
    });
  } else {
    throw new Error('Upstash environment variables not set');
  }
} catch (err) {
  console.warn('[AI Studio] Upstash Redis not configured — using in-memory mock');
  const store = new Map();
  redis = {
    get: async (k) => store.get(k) ?? null,
    set: async (k, v) => { store.set(k, v); return 'OK'; },
    del: async (k) => store.delete(k),
    incr: async (k) => { const n = (store.get(k) || 0) + 1; store.set(k, n); return n; },
  };
  defaultLimiter = {
    limit: async () => ({ success: true, limit: 100, remaining: 99, reset: Date.now() + 60000 }),
  };
}

// Factory to create per-route / per-purpose rate limiters sharing the same Redis instance.
function createRatelimit(points = 100, window = '1 m', analytics = false) {
  if (process.env.UPSTASH_REDIS_REST_URL && process.env.UPSTASH_REDIS_REST_TOKEN && redis && typeof redis.eval === 'function') {
    try {
      return new Ratelimit({
        redis,
        limiter: Ratelimit.slidingWindow(points, window),
        analytics,
      });
    } catch (e) {
      console.warn('[AI Studio] Ratelimit init failed, using fallback:', e.message);
    }
  }
  return {
    limit: async () => ({ success: true, limit: points, remaining: points - 1, reset: Date.now() + 60000 }),
  };
}

module.exports = { redis, createRatelimit, defaultLimiter };