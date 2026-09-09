import re

with open("frontend/src/pages/RoleDashboard.jsx", "r") as f:
    content = f.read()

# Make the wrapper scrollable
# Old wrapper:
# <div className="flex-1 overflow-hidden flex flex-col bg-slate-50/50 dark:bg-slate-900/50">
old_wrapper = '<div className="flex-1 overflow-hidden flex flex-col bg-slate-50/50 dark:bg-slate-900/50">'
new_wrapper = '<div className="flex-1 overflow-y-auto flex flex-col bg-slate-50/50 dark:bg-slate-900/50">'

content = content.replace(old_wrapper, new_wrapper)

with open("frontend/src/pages/RoleDashboard.jsx", "w") as f:
    f.write(content)

print("Scroll fixed")
