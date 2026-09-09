import re

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

# We need to extract the search block and move it before the status filter block.
search_block_regex = r"(\s*{/\* Search \*/}\s*<div className=\"relative\">\s*<Search className=\"[^\"]+\" />\s*<input[^>]+>\s*</div>)"

match = re.search(search_block_regex, content)
if not match:
    print("Search block not found")
else:
    search_block = match.group(1)
    
    # Remove search block from current position
    content = content.replace(search_block, "")
    
    # Insert search block before Status Filter
    status_filter_marker = "{/* Status Filter */}"
    content = content.replace(status_filter_marker, search_block.strip() + "\n\n          " + status_filter_marker)
    
    # To put a spacer after route filter and before view toggle... Wait, is it a spacer? 
    # "Route: All -> (spacer) -> view toggle -> Add Unit."
    # If the container is `justify-between` or something, we can use `mr-auto` on Route filter or `ml-auto` on view toggle.
    # Currently it's `justify-end items-stretch sm:items-center gap-3`. If we put `mr-auto` on the first 3 items wrapper?
    # Or maybe the container should just be `flex flex-col sm:flex-row items-stretch sm:items-center gap-3 w-full`.
    # And we add `ml-auto` to the `View Toggle` div.
    
    with open("frontend/src/pages/admin/UnitManagementPage.jsx", "w") as f:
        f.write(content)
    print("Successfully moved search block.")
