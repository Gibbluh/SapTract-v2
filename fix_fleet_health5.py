import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# Using regex to remove from <div className="w-full grid grid-cols-2 gap-3 mb-6 pointer-events-auto"> up to the end of the widget
regex = r'          <div className="w-full grid grid-cols-2 gap-3 mb-6 pointer-events-auto">.*?</svg>\s*</div>\s*<span className="text-xs font-bold dark:text-slate-500 text-slate-700">\{idle\} units</span>\s*</div>\s*</div>'

# Okay regex is too brittle. I will literally split it using a safe string
parts = content.split('<div className="w-full grid grid-cols-2 gap-3 mb-6 pointer-events-auto">')

if len(parts) > 1:
    before = parts[0]
    # Find the next widget start to know where this one ends
    after_parts = parts[1].split('    \'chart-dispatches\': (')
    if len(after_parts) > 1:
        new_content = before + '        </div>\n          ),\n    \'chart-dispatches\': (' + after_parts[1]
        with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
            f.write(new_content)
