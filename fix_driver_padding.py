import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# Reduce padding on chart-dispatches and chart-fleet to compact them
# from p-6 to p-5 to save some vertical space
content = content.replace(
    "'chart-dispatches': (\n        <div className=\"dark:bg-slate-800 bg-white border dark:border-slate-700 border-slate-200 rounded-3xl p-6 shadow-sm",
    "'chart-dispatches': (\n        <div className=\"dark:bg-slate-800 bg-white border dark:border-slate-700 border-slate-200 rounded-3xl p-5 shadow-sm"
)

content = content.replace(
    "'chart-fleet': (\n        <div className=\"dark:bg-slate-800 bg-white border dark:border-slate-700 border-slate-200 rounded-3xl p-6 shadow-sm",
    "'chart-fleet': (\n        <div className=\"dark:bg-slate-800 bg-white border dark:border-slate-700 border-slate-200 rounded-3xl p-5 shadow-sm"
)

# And reduce maxHeight of driver list from 180px to 150px
content = content.replace("maxHeight: '180px'", "maxHeight: '150px'")

# Actually, the image shows Today's Driver having p-5 or p-6, but let's just make the driver list flex-1 instead of fixed height so it fills the available space
# Wait, if we use flex-1 min-h-0, it will shrink to fit the grid row!
# Let's see if we can do that.
# Find: <div className="flex flex-col gap-3 overflow-y-auto pr-2 relative z-20" style={{ maxHeight: '150px' }} onPointerDown={(e) => e.stopPropagation()}>
# Replace with: <div className="flex flex-col gap-3 overflow-y-auto pr-2 relative z-20 flex-1 min-h-0" onPointerDown={(e) => e.stopPropagation()}>

content = re.sub(
    r'<div className="flex flex-col gap-3 overflow-y-auto pr-2 relative z-20" style=\{\{ maxHeight: \'\d+px\' \}\} onPointerDown=\{\(e\) => e.stopPropagation\(\)\}>',
    '<div className="flex flex-col gap-3 overflow-y-auto pr-2 relative z-20 flex-1 min-h-[150px]" onPointerDown={(e) => e.stopPropagation()}>',
    content
)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
