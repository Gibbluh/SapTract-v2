with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    lines = f.readlines()

# The bad line is line 472 (index 471) -> "        </div>\n"
lines.pop(471)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.writelines(lines)
