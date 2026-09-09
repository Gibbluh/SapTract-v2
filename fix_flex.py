import re

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

# Replace flex-col xl:flex-row with flex-col lg:flex-row items-stretch lg:items-center
content = content.replace(
    'className="flex flex-col xl:flex-row items-center gap-4 mb-6"',
    'className="flex flex-col lg:flex-row items-stretch lg:items-center gap-4 mb-6"'
)

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "w") as f:
    f.write(content)
