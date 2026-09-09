import re

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

# 1. Extract the Filters block
filters_pattern = r'\{/\* Filters and Actions Toolbar \*/\}.*?(?=\{/\* Route Summary Card \*/\}|<div className="grid grid-cols-1)'
filters_match = re.search(filters_pattern, content, flags=re.DOTALL)
if filters_match:
    filters_code = filters_match.group(0)

# We will remove the old filters block
main_start = content.find('<main className="flex-1 p-6 overflow-auto">')
after_main = content[main_start + len('<main className="flex-1 p-6 overflow-auto">'):]
after_main = after_main.replace(filters_code, '')

# Now let's extract the individual pieces from filters_code
status_start = filters_code.find('{/* Status Dropdown Filter */}')
route_start = filters_code.find('{/* Route Dropdown Filter */}')
search_start = filters_code.find('{/* Search Input (Takes up available space) */}')
view_toggle_start = filters_code.find('{/* View Toggle */}')
add_unit_start = filters_code.find('{/* Add Unit */}')

status_block = filters_code[status_start:route_start].strip()
route_block = filters_code[route_start:search_start].strip()
search_block = filters_code[search_start:view_toggle_start].strip()

# view_toggle_block needs to be extracted carefully since it's the last element of the flex container
# I'll just regex it or find the closing tags.
view_toggle_match = re.search(r'\{/\* View Toggle \*/\}.*?(?=\{/\* Add Unit \*/\})', filters_code, flags=re.DOTALL)
view_toggle_block = view_toggle_match.group(0).strip() if view_toggle_match else ""

# 2. Build the new layout
new_top_section = f"""
        {{/* Page Header */}}
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6">
          <div>
            <div className="flex items-center gap-1.5 text-[11px] font-medium text-slate-500 mb-1">
              <span>SPTC</span>
              <span className="opacity-50">/</span>
              <span>Fleet Vehicles</span>
              <span className="opacity-50">/</span>
              <span className="font-semibold text-slate-700">Modern Jeepneys</span>
            </div>
            <h1 className="text-2xl font-bold text-slate-900 tracking-tight">Unit Management</h1>
          </div>
          <button 
            onClick={{() => setFormOpen(true)}}
            className="px-5 py-2.5 bg-blue-600 text-white rounded-lg text-sm font-bold hover:bg-blue-700 transition-colors shadow-sm flex items-center gap-2 whitespace-nowrap"
          >
            <Plus className="w-4 h-4" /> Add Unit
          </button>
        </div>

        {{/* Filters Toolbar Card */}}
        <div className="bg-white border border-gray-200 rounded-xl p-3 shadow-sm flex flex-col lg:flex-row items-stretch lg:items-center gap-3 mb-6">
          {status_block}
          {route_block}
          {search_block}
          <div className="flex items-center gap-3 shrink-0 lg:ml-auto">
            {view_toggle_block}
          </div>
        </div>
"""

new_content = content[:main_start + len('<main className="flex-1 p-6 overflow-auto">')] + new_top_section + after_main

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "w") as f:
    f.write(new_content)
print("Layout updated.")
