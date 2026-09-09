import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# I also need to remove pieData and COLORS if they are no longer used since we changed chart-fleet
if "PieChart" not in content and "pieData" in content:
    content = re.sub(r"  const pieData = \[.*?\];\n  const COLORS = \['#10b981', '#f59e0b', '#ef4444', '#94a3b8'\];\n", "", content, flags=re.DOTALL)
    
with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
