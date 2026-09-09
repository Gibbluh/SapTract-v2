import re

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

# We need to extract the search block and move it before the status filter block.
search_block_regex = r"(\s*{/\* Search \*/}\s*<div className=\"relative\">.*?</div>)"

match = re.search(search_block_regex, content, re.DOTALL)
if not match:
    print("Search block not found")
else:
    search_block = match.group(1)
    
    # Remove search block from current position
    content = content.replace(search_block, "")
    
    # Insert search block before Status Filter
    status_filter_marker = "{/* Status Filter */}"
    content = content.replace(status_filter_marker, search_block.strip() + "\n\n          " + status_filter_marker)
    
    # To put a spacer:
    # First, let's find the container `flex flex-col sm:flex-row justify-end ...`
    # Replace it to be w-full, remove justify-end
    content = content.replace(
        '<div className="flex flex-col sm:flex-row justify-end items-stretch sm:items-center gap-3">',
        '<div className="flex flex-col sm:flex-row items-stretch sm:items-center gap-3 w-full justify-between">'
    )
    
    # Actually wait. If it's justify-between, and there are 5 children:
    # 1. Search
    # 2. Status
    # 3. Route
    # 4. View Toggle
    # 5. Add Unit
    # Then `justify-between` will space them all out evenly. We don't want that!
    # We want: Search, Status, Route aligned left. (Spacer). View Toggle, Add Unit aligned right.
    # We can do this by wrapping the first three in a div, and the last two in a div?
    # No, we can just add `ml-auto` to the `View Toggle` container!
    
    content = content.replace(
        '<div className="flex flex-col sm:flex-row justify-end items-stretch sm:items-center gap-3">',
        '<div className="flex flex-col sm:flex-row items-stretch sm:items-center gap-3 w-full">'
    )
    
    content = content.replace(
        '{/* View Toggle */}',
        '{/* View Toggle */}\n          <div className="flex items-center gap-3 sm:ml-auto">'
    )
    
    # Wait, we need to wrap both View Toggle and Add Unit button in the sm:ml-auto flex div.
    # Or simply add `sm:ml-auto` to the View Toggle div, and keep Add Unit where it is. If View Toggle has sm:ml-auto, it pushes itself and everything after it to the right!
    content = content.replace(
        '<div className="flex bg-gray-100 rounded-lg p-1">',
        '<div className="flex bg-gray-100 rounded-lg p-1 sm:ml-auto">'
    )

    with open("frontend/src/pages/admin/UnitManagementPage.jsx", "w") as f:
        f.write(content)
    print("Successfully moved search block.")
