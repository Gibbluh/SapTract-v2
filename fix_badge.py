import re

with open('frontend/src/components/layout/Sidebar.jsx', 'r') as f:
    content = f.read()

# Make sure overflow-x-hidden is removed from the nav container so badge isn't cut off if it extends slightly
content = content.replace('nav className="px-2.5 flex-1 min-h-0 overflow-y-auto overflow-x-hidden py-3 space-y-1"', 'nav className="px-2.5 flex-1 min-h-0 overflow-y-auto py-3 space-y-1"')

# Change badge to be exactly top-0 right-0 instead of top-1 right-1 so it sits higher
content = content.replace('<span className="absolute top-1 right-1 flex h-4 w-4 items-center justify-center rounded-full bg-red-600 text-[9px] font-bold text-white border-2 border-[#1B3679] shadow-sm z-10">', '<span className="absolute -top-0.5 -right-0.5 flex h-4 w-4 items-center justify-center rounded-full bg-red-600 text-[9px] font-bold text-white border border-[#1B3679] shadow-sm z-10">')

with open('frontend/src/components/layout/Sidebar.jsx', 'w') as f:
    f.write(content)
