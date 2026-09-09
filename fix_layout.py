import re

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

# First, locate the <header> block.
header_start = content.find('{/* HEADER BAR */}')
main_start = content.find('<main className="flex-1 p-6 overflow-auto">')

if header_start != -1 and main_start != -1:
    # Everything from header_start to main_start
    header_block = content[header_start:main_start]
    
    # We need to extract the Status and Route dropdowns.
    status_filter_idx = header_block.find('{/* Status Dropdown Filter */}')
    route_filter_idx = header_block.find('{/* Route Dropdown Filter */}')
    view_toggle_idx = header_block.find('{/* View Toggle */}')
    add_unit_idx = header_block.find('{/* Add Unit */}')
    
    status_block = header_block[status_filter_idx:route_filter_idx].strip()
    route_block = header_block[route_filter_idx:view_toggle_idx].strip()
    
    # Actually, extracting via regex might be safer.
