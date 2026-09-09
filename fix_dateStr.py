import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# Check if dateStr is used
if "dateStr" not in content.replace("const dateStr = todayDate.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });", ""):
    content = content.replace("const todayDate = new Date();\n  const dateStr = todayDate.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });\n", "")

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
