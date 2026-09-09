import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# 1. Fix massive gap by letting chart fill the space
content = content.replace(
    '<div className="relative h-64 w-full mb-4 relative z-10"',
    '<div className="relative flex-1 min-h-[200px] w-full mb-4 z-10"'
)
# (Also the string had `relative` twice in `relative h-64 w-full mb-4 relative z-10`? Let's be safe)
content = content.replace(
    '<div className="relative h-64 w-full mb-4 relative z-10" onPointerDown={(e) => e.stopPropagation()}>',
    '<div className="relative flex-1 min-h-[150px] w-full mb-4 z-10" onPointerDown={(e) => e.stopPropagation()}>'
)

# Wait, let's look at the exact line 349:
# <div className="relative h-64 w-full mb-4 relative z-10" onPointerDown={(e) => e.stopPropagation()}>

# 2. Fix the Total Trips label which squished the 3rd column
content = content.replace(
    '<p className="text-xs dark:text-slate-400 text-slate-500 font-semibold whitespace-nowrap">Total Trips Completed</p>',
    '<p className="text-xs dark:text-slate-400 text-slate-500 font-semibold whitespace-nowrap">Total Trips</p>'
)

# 3. Ensure Fuel Efficiency value doesn't wrap
content = content.replace(
    '<p className="text-base font-bold dark:text-white text-slate-900 flex items-baseline gap-1">\n                  4.2 km/L',
    '<p className="text-base font-bold dark:text-white text-slate-900 flex items-baseline flex-wrap xl:flex-nowrap gap-1">\n                  <span className="whitespace-nowrap">4.2 km/L</span>'
)

# 4. Same for Average Per Trip just in case
content = content.replace(
    '<p className="text-base font-bold dark:text-white text-slate-900 flex items-baseline gap-1">\n                  ₱384',
    '<p className="text-base font-bold dark:text-white text-slate-900 flex items-baseline flex-wrap xl:flex-nowrap gap-1">\n                  <span className="whitespace-nowrap">₱384</span>'
)

# 5. Same for Total Trips just in case
content = content.replace(
    '<p className="text-base font-bold dark:text-white text-slate-900 flex items-baseline gap-1">\n                  {324 * tfMult}',
    '<p className="text-base font-bold dark:text-white text-slate-900 flex items-baseline flex-wrap xl:flex-nowrap gap-1">\n                  <span className="whitespace-nowrap">{324 * tfMult}</span>'
)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
