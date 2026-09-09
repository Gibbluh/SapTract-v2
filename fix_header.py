import re

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

# Replace the inner container class to not be justify-end
content = content.replace(
    '<div className="flex flex-col sm:flex-row items-center gap-3 flex-1 justify-end">',
    '<div className="flex flex-col sm:flex-row items-center gap-3 flex-1">'
)

# Fix the duplicate div issue I introduced:
content = content.replace(
    '<div className="flex items-center gap-3 sm:ml-auto">\n          <div className="flex bg-gray-100 rounded-lg p-1 sm:ml-auto">',
    '<div className="flex items-center gap-3 sm:ml-auto">\n          {/* View Toggle */}\n          <div className="flex bg-gray-100 rounded-lg p-1">'
)
# Note: In my previous python script I did:
# content = content.replace(
#    '{/* View Toggle */}',
#    '{/* View Toggle */}\n          <div className="flex items-center gap-3 sm:ml-auto">'
# )
# And then:
# content = content.replace(
#    '<div className="flex bg-gray-100 rounded-lg p-1">',
#    '<div className="flex bg-gray-100 rounded-lg p-1 sm:ml-auto">'
# )

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "w") as f:
    f.write(content)
print("done")
