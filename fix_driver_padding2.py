import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

content = content.replace(
    '<div className="flex flex-col gap-3 overflow-y-auto pr-2 relative z-20 flex-1 min-h-[150px]" onPointerDown={(e) => e.stopPropagation()}>',
    '<div className="flex flex-col gap-3 overflow-y-auto pr-2 relative z-20 flex-1" style={{ maxHeight: "140px" }} onPointerDown={(e) => e.stopPropagation()}>'
)

# And let's remove some bottom margin from chart-fleet elements
content = content.replace('mb-6', 'mb-4')

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
