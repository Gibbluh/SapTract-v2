import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# Fix Today's Driver - remove fixed maxHeight and add min-h-0 to allow it to fill flex-1
content = content.replace(
    '<div className="flex flex-col gap-2 overflow-y-auto pr-1 relative z-20 flex-1" style={{ maxHeight: "140px" }} onPointerDown={(e) => e.stopPropagation()}>',
    '<div className="flex flex-col gap-2 overflow-y-auto pr-1 relative z-20 flex-1 min-h-0" onPointerDown={(e) => e.stopPropagation()}>'
)

# Fix Fleet Health - use justify-between to spread out the content if it gets tall, or just remove mb-4 and use justify-evenly
content = content.replace(
    '<div className="w-full flex-1 flex flex-col justify-center mb-4 pointer-events-auto" onPointerDown={(e) => e.stopPropagation()}>',
    '<div className="w-full flex-1 flex flex-col justify-evenly pointer-events-auto" onPointerDown={(e) => e.stopPropagation()}>'
)
# Remove the mt-4 mb-3 from the health bar so justify-evenly handles the spacing
content = content.replace(
    '<div className="w-full h-4 rounded-full overflow-hidden flex bg-slate-100 dark:bg-slate-700 mt-4 mb-3 border dark:border-slate-600 border-slate-200">',
    '<div className="w-full h-4 rounded-full overflow-hidden flex bg-slate-100 dark:bg-slate-700 border dark:border-slate-600 border-slate-200">'
)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
