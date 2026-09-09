import re

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

# Let's extract the actual whole block for Filters and Search.
start_marker = "{/* Filters and Search */}"
end_marker = "{/* Bulk Actions Bar */}"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Markers not found")
else:
    print("Markers found")
