import re

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

# Extract Status Filter
status_start = content.find('{/* Status Dropdown Filter */}')
route_start = content.find('{/* Route Dropdown Filter */}')
status_block = content[status_start:route_start].strip()

# Extract Route Filter
view_toggle_start = content.find('{/* View Toggle */}')
route_block = content[route_start:view_toggle_start].strip()

# Create the new toolbar
new_toolbar = f"""        {{/* Filters and Actions Toolbar */}}
        <div className="flex flex-col xl:flex-row items-center gap-4 mb-6">
          {status_block}

          {route_block}

          {{/* Search Input (Takes up available space) */}}
          <div className="relative flex-1 w-full min-w-[200px]">
            <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" />
            <input 
              type="text" 
              placeholder="Search plate, unit..." 
              value={{searchQuery}}
              onChange={{(e) => setSearchQuery(e.target.value)}}
              className="bg-white text-gray-900 placeholder-gray-400 pl-9 pr-4 py-2.5 border border-gray-300 rounded-lg text-sm w-full focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-shadow shadow-sm"
            />
          </div>

          <div className="flex items-center gap-4 w-full xl:w-auto shrink-0 justify-end">
            {{/* View Toggle */}}
            <div className="flex bg-white border border-gray-200 rounded-lg p-1 shadow-sm">
              <button
                title="Grid View"
                onClick={{() => setViewMode('grid')}}
                className={{`p-1.5 rounded-md transition-colors ${{viewMode === 'grid' ? 'bg-slate-100 text-blue-600' : 'text-gray-500 hover:text-gray-700 hover:bg-slate-50'}}`}}
              >
                <LayoutGrid className="w-4 h-4" />
              </button>
              <button
                title="Table View"
                onClick={{() => setViewMode('table')}}
                className={{`p-1.5 rounded-md transition-colors ${{viewMode === 'table' ? 'bg-slate-100 text-blue-600' : 'text-gray-500 hover:text-gray-700 hover:bg-slate-50'}}`}}
              >
                <List className="w-4 h-4" />
              </button>
            </div>

            {{/* Add Unit */}}
            <button 
              onClick={{() => setFormOpen(true)}}
              className="px-5 py-2.5 bg-blue-600 text-white rounded-lg text-sm font-bold hover:bg-blue-700 transition-colors shadow-sm flex items-center gap-2 whitespace-nowrap"
            >
              <Plus className="w-4 h-4" /> Add Unit
            </button>
          </div>
        </div>"""

# Remove the old header.
header_start = content.find('{/* HEADER BAR */}')
main_start = content.find('<main className="flex-1 p-6 overflow-auto">')

if header_start != -1 and main_start != -1:
    content = content[:header_start] + content[main_start:]

# Inject new toolbar right after <main ...>
main_tag = '<main className="flex-1 p-6 overflow-auto">'
content = content.replace(main_tag, f'{main_tag}\n{new_toolbar}')

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "w") as f:
    f.write(content)
print("done")
