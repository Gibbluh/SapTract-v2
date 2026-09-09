import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# 1. Remove Live Feed badge
content = content.replace(
    '<span className="dark:bg-blue-900/50 bg-blue-50 dark:text-blue-400 text-blue-600 text-xs font-semibold px-2.5 py-0.5 rounded-full border dark:border-blue-800 border-blue-100">Live Feed</span>',
    ''
)

# 2. Remove subtitle description
content = content.replace(
    '<p className="text-xs dark:text-slate-400 text-slate-500 mb-4">Real-time gross passenger fares & collection analytics</p>',
    ''
)

# 3. Remove info hover text
content = re.sub(
    r'<div className="absolute top-0 left-0 flex items-center dark:text-slate-500 text-slate-400 text-xs">.*?Hover across timeline curve for interval revenue breakdown.*?</div>',
    '',
    content,
    flags=re.DOTALL
)

# 4. Remove grey background from metric cards and make text one-line
# Replace card containers
content = content.replace(
    '<div className="flex items-center gap-3 dark:bg-slate-900/50 bg-slate-50/50 rounded-xl p-3 border dark:border-slate-700 border-slate-100">',
    '<div className="flex items-center gap-3">'
)

content = content.replace(
    '<p className="text-[10px] dark:text-slate-400 text-slate-500 font-medium">Average Per Trip</p>',
    '<p className="text-[11px] dark:text-slate-400 text-slate-500 font-semibold whitespace-nowrap">Average Per Trip</p>'
)

content = content.replace(
    '<p className="text-[10px] dark:text-slate-400 text-slate-500 font-medium">Total Trips Completed</p>',
    '<p className="text-[11px] dark:text-slate-400 text-slate-500 font-semibold whitespace-nowrap">Total Trips</p>'
)

content = content.replace(
    '<p className="text-[10px] dark:text-slate-400 text-slate-500 font-medium">Fuel Efficiency</p>',
    '<p className="text-[11px] dark:text-slate-400 text-slate-500 font-semibold whitespace-nowrap">Fuel Efficiency</p>'
)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
