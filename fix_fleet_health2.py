import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

fleet_bottom_regex = r'          <div className="w-full grid grid-cols-2 gap-3 mb-6 pointer-events-auto">.*?<div className="flex items-center text-xs font-medium dark:text-slate-300 text-slate-700">.*?Idle.*?</div>\s*<span className="text-xs font-bold dark:text-slate-500 text-slate-700">\{idle\} units</span>\s*</div>\s*</div>\s*</div>'

new_bottom = """        </div>"""

content = re.sub(fleet_bottom_regex, new_bottom, content, flags=re.DOTALL)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
