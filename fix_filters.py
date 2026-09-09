import re

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

# Replace the filter row div classes
old_class = 'className="bg-white border border-gray-200 rounded-xl p-3 shadow-sm flex flex-col lg:flex-row items-stretch lg:items-center gap-3 mb-6"'
new_class = 'className="flex flex-wrap items-center gap-3 mb-6"'

content = content.replace(old_class, new_class)

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "w") as f:
    f.write(content)

print("Fixed")
