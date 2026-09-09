import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

content = content.replace("  PieChart,\n  Pie,\n  Cell\n", "")

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
