import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# Average Per Trip Icon
content = re.sub(
    r'<div className="w-10 h-10 dark:bg-blue-900/50 bg-blue-50 dark:text-blue-400 text-blue-500 rounded-lg flex items-center justify-center shrink-0">\s*<TrendingUp className="w-5 h-5" />\s*</div>\s*',
    '',
    content
)

# Total Trips Icon
content = re.sub(
    r'<div className="w-10 h-10 dark:bg-emerald-900/50 bg-emerald-50 dark:text-emerald-400 text-emerald-500 rounded-lg flex items-center justify-center shrink-0">\s*<Activity className="w-5 h-5" />\s*</div>\s*',
    '',
    content
)

# Fuel Efficiency Icon
content = re.sub(
    r'<div className="w-10 h-10 dark:bg-amber-900/50 bg-amber-50 dark:text-amber-400 text-amber-500 rounded-lg flex items-center justify-center shrink-0">\s*<Fuel className="w-5 h-5" />\s*</div>\s*',
    '',
    content
)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
