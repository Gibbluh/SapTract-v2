with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

content = content.replace(
    'className="flex items-center gap-4 w-full xl:w-auto shrink-0 justify-end"',
    'className="flex items-center gap-4 w-full lg:w-auto shrink-0 justify-end lg:justify-start"'
)

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "w") as f:
    f.write(content)
