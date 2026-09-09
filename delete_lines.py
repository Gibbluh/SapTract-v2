with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    lines = f.readlines()

# The bad block is between lines 471 and 484
lines = lines[:471] + lines[483:]

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.writelines(lines)
