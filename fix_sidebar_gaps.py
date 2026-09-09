import re

with open('frontend/src/components/layout/Sidebar.jsx', 'r') as f:
    content = f.read()

# Fix Sidebar nav gaps completely by removing category margins and applying a unified margin-bottom
# 1. Remove space-y-1 from nav
content = content.replace('nav className="px-2.5 flex-1 min-h-0 overflow-y-auto py-3 space-y-1"', 'nav className="px-2.5 flex-1 min-h-0 overflow-y-auto py-3"')

# 2. Change category header to have NO height when collapsed so it doesn't cause extra space
content = content.replace('className={idx !== 0 ? "mt-1" : ""}', 'className="flex flex-col"')
content = content.replace('className={`px-3 text-xs font-bold text-white tracking-wider transition-all duration-300 ease-in-out overflow-hidden whitespace-nowrap ${', 'className={`px-3 font-bold text-white tracking-wider transition-all duration-300 ease-in-out overflow-hidden whitespace-nowrap ${')
content = content.replace('isExpanded\n                        ? "pb-1.5 opacity-100 max-w-[170px]"', 'isExpanded\n                        ? "text-xs pt-3 pb-1.5 opacity-100 max-w-[170px]"')
content = content.replace('                        : "opacity-0 max-w-0 pointer-events-none"', '                        : "text-[0px] h-0 opacity-0 max-w-0 pointer-events-none"')

# 3. Add mb-1 to NavLink to handle all gaps
content = content.replace('transition-all duration-150 border-l-4 ${', 'transition-all duration-150 border-l-4 mb-1 ${')

with open('frontend/src/components/layout/Sidebar.jsx', 'w') as f:
    f.write(content)
