import re

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

# Make search and buttons shrink to fit like before
content = content.replace('<div className="relative">', '<div className="relative shrink-0">')
content = content.replace('<div className="relative flex-1 sm:max-w-xs">', '<div className="relative flex-1 sm:max-w-xs shrink-0">')
content = content.replace('<div className="flex items-center bg-gray-100 rounded-lg p-1">', '<div className="flex items-center bg-gray-100 rounded-lg p-1 shrink-0">')
content = content.replace('className="px-5 py-2.5 bg-blue-600 text-white rounded-lg text-sm font-bold hover:bg-blue-700 transition-colors flex items-center gap-2 whitespace-nowrap shadow-sm"', 'className="px-5 py-2 bg-blue-600 text-white rounded-lg text-sm font-bold hover:bg-blue-700 transition-colors flex items-center gap-2 whitespace-nowrap shrink-0 shadow-sm"')
content = content.replace('{/* Search Input */}', '<div className="flex-1"></div>\n          {/* Search Input */}')

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "w") as f:
    f.write(content)

print("Fixed")
