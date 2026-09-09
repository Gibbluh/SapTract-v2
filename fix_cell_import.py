import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

content = content.replace("  Bar,\n  XAxis,", "  Bar,\n  Cell,\n  XAxis,")

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
