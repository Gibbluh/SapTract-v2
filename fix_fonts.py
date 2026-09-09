import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# Fix chart-dispatches fonts & sizing
# Header size
content = content.replace(
    '<h2 className="text-lg font-bold dark:text-white text-slate-900 flex items-center gap-2">',
    '<h2 className="text-base font-bold dark:text-white text-slate-900 flex items-center gap-2">'
)
# Activity Icon
content = content.replace(
    '<Activity className="w-5 h-5 dark:text-blue-400 text-blue-500" />',
    '<Activity className="w-4 h-4 dark:text-blue-400 text-blue-500" />'
)
# Active Driver count text
content = content.replace(
    '<div className="flex items-center text-sm font-bold text-blue-600 dark:text-blue-400">',
    '<div className="flex items-center text-xs font-bold text-blue-600 dark:text-blue-400">'
)
# List gap
content = content.replace(
    '<div className="flex flex-col gap-3 overflow-y-auto pr-2 relative z-20 flex-1"',
    '<div className="flex flex-col gap-2 overflow-y-auto pr-1 relative z-20 flex-1"'
)
# Driver list item padding & radius
content = content.replace(
    '<div key={driver.id} className="flex items-center p-3 rounded-2xl',
    '<div key={driver.id} className="flex items-center p-2 rounded-xl'
)
# Avatar container margin
content = content.replace(
    '<div className="relative shrink-0 mr-4">',
    '<div className="relative shrink-0 mr-3">'
)
# Avatar image size
content = content.replace(
    'className="w-12 h-12 rounded-full object-cover',
    'className="w-10 h-10 rounded-full object-cover'
)
# Status dot size
content = content.replace(
    '<span className="absolute bottom-0 right-0 w-3.5 h-3.5',
    '<span className="absolute bottom-0 right-0 w-3 h-3'
)
# Driver name font
content = content.replace(
    '<h4 className="text-sm font-bold dark:text-white text-slate-900 truncate">{driver.name}</h4>',
    '<h4 className="text-xs font-bold dark:text-white text-slate-900 truncate">{driver.name}</h4>'
)
# Driver text
content = content.replace(
    '<div className="flex items-center text-[11px] font-medium text-slate-500 dark:text-slate-400 gap-2 mt-0.5">',
    '<div className="flex items-center text-[10px] font-medium text-slate-500 dark:text-slate-400 gap-1.5 mt-0.5">'
)


# Fix chart-fleet fonts & sizing
# Header
content = content.replace(
    '<h2 className="text-lg font-bold dark:text-white text-slate-900 flex items-center gap-1">',
    '<h2 className="text-base font-bold dark:text-white text-slate-900 flex items-center gap-1">'
)
# Good Standby label
content = content.replace(
    '<span className="dark:bg-emerald-900/50 bg-emerald-50 dark:text-emerald-400 text-emerald-600 text-xs font-semibold px-2.5 py-0.5 rounded-full border dark:border-emerald-800 border-emerald-100">Good Standby</span>',
    '<span className="flex flex-col text-right leading-tight dark:text-emerald-400 text-emerald-600 text-[10px] font-semibold bg-emerald-50 dark:bg-emerald-900/30 px-2 py-0.5 rounded-full border border-emerald-100 dark:border-emerald-800/50">Good<br/>Standby</span>'
)
content = content.replace(
    '<div className="w-full flex justify-between items-center mb-4">',
    '<div className="w-full flex justify-between items-start mb-4">'
)
# 85% Score
content = content.replace(
    '<span className="text-4xl font-black dark:text-white text-slate-900 tracking-tight">85%</span>',
    '<span className="text-3xl font-black dark:text-white text-slate-900 tracking-tight">85%</span>'
)
# Units text
content = content.replace(
    '<p className="text-[11px] font-semibold dark:text-slate-300 text-slate-700">20 / 25 Units</p>',
    '<p className="text-[10px] font-semibold dark:text-slate-300 text-slate-700">20 / 25 Units</p>'
)
# Units subtext
content = content.replace(
    '<p className="text-[10px] dark:text-slate-500 text-slate-500">Road-ready for peak commute</p>',
    '<p className="text-[9px] dark:text-slate-500 text-slate-500">Road-ready for peak commute</p>'
)
# Legend text
content = content.replace(
    '<div className="flex justify-between items-center text-[10px] font-medium px-1">',
    '<div className="flex justify-between items-center text-[9px] font-medium px-1">'
)


with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
