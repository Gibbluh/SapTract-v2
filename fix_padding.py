import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

content = content.replace(
    "'chart-fleet': (\n              <div className=\"dark:bg-slate-800 bg-white border dark:border-slate-700 border-slate-200 rounded-3xl p-6",
    "'chart-fleet': (\n              <div className=\"dark:bg-slate-800 bg-white border dark:border-slate-700 border-slate-200 rounded-3xl p-5"
)

content = content.replace(
    "'chart-dispatches': (\n        <div className=\"dark:bg-slate-800 bg-white border dark:border-slate-700 border-slate-200 rounded-3xl p-6 shadow-sm flex flex-col w-full h-full cursor-grab active:cursor-grabbing pointer-events-auto\">",
    "'chart-dispatches': (\n        <div className=\"dark:bg-slate-800 bg-white border dark:border-slate-700 border-slate-200 rounded-3xl p-5 shadow-sm flex flex-col w-full h-full cursor-grab active:cursor-grabbing pointer-events-auto\">"
)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
