with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

# I will replace the exact text of the extra opening div with an empty string
bad_div = '<div className="flex items-center gap-4 w-full lg:w-auto shrink-0 justify-end lg:justify-start">'
if bad_div in content:
    content = content.replace(bad_div, '')

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "w") as f:
    f.write(content)
print("Fixed.")
