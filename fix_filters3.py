import re

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

# Add the white container back to the entire block
old_filter_block = """{/* Filters Toolbar Card */}
        <div className="flex flex-wrap items-center gap-3 mb-6">"""

new_filter_block = """{/* Filters Toolbar Card */}
        <div className="bg-white border border-gray-200 rounded-xl p-3 shadow-sm flex flex-wrap items-center gap-3 mb-6">"""

content = content.replace(old_filter_block, new_filter_block)

# Fix relative containers
content = content.replace('<div className="relative">', '<div className="relative shrink-0">')
content = content.replace('<div className="relative shrink-0">\n            <Search', '<div className="relative flex-1 sm:max-w-xs shrink-0">\n            <Search')
content = content.replace('<div className="flex items-center bg-gray-100 rounded-lg p-1">', '<div className="flex items-center bg-gray-100 rounded-lg p-1 shrink-0">')


with open("frontend/src/pages/admin/UnitManagementPage.jsx", "w") as f:
    f.write(content)

print("Fixed")
