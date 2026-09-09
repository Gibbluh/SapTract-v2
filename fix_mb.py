import re
with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()
content = content.replace('<div className="flex justify-between items-end mb-2">', '<div className="flex justify-between items-end">')
with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
