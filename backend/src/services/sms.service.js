const axios = require('axios');

const sendSMS = async ({ number, message }) => {
  if (!number) {
    throw new Error('Driver phone number is missing.');
  }

  if (!process.env.ANDROID_SMS_GATEWAY_URL) {
    console.log(`[SMS Service] Gateway not configured. Mocking SMS to ${number}: ${message}`);
    return { success: true, mocked: true };
  }

  const response = await axios.post(
    process.env.ANDROID_SMS_GATEWAY_URL,
    {
      number,
      message,
    },
    {
      headers: {
        Authorization: `Bearer ${process.env.ANDROID_SMS_GATEWAY_TOKEN}`,
        'Content-Type': 'application/json',
      },
      timeout: 4000,
    }
  );

  return response.data;
};

module.exports = {
  sendSMS,
};