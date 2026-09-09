import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# Fix chart-dispatches header
content = content.replace(
    '<div className="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-4 gap-3">',
    '<div className="flex flex-col xl:flex-row justify-between items-start xl:items-center mb-4 gap-3">'
)

# Fix chart-fleet header
# Assuming it also uses the same classes
content = content.replace(
    '<div className="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-2 gap-3">',
    '<div className="flex flex-col xl:flex-row justify-between items-start xl:items-center mb-2 gap-3">'
)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
