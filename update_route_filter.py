import re

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

# The Route Filter Dropdown HTML to insert before Search
route_dropdown_html = """          {/* Route Dropdown Filter */}
          <div className="relative">
            <button
              onClick={() => setRouteDropdownOpen(!routeDropdownOpen)}
              className="px-4 py-2 bg-white border border-gray-300 rounded-lg text-sm font-medium text-gray-700 hover:bg-gray-50 flex items-center gap-2 transition-colors"
            >
              <Filter className="w-4 h-4 text-gray-400" />
              Route: {routeFilter}
              <ChevronDown className="w-4 h-4 text-gray-400 ml-1" />
            </button>
            
            {routeDropdownOpen && (
              <>
                <div className="fixed inset-0 z-40" onClick={() => setRouteDropdownOpen(false)}></div>
                <div className="absolute top-full mt-2 left-0 sm:right-0 sm:left-auto w-56 bg-white border border-gray-200 rounded-xl shadow-lg z-50 py-1 flex flex-col">
                  <div className="px-3 py-2 text-xs font-semibold text-gray-500 uppercase tracking-wider border-b border-gray-100">
                    Filter by Route
                  </div>
                  <button
                    onClick={() => { setRouteFilter('All'); setRouteDropdownOpen(false); }}
                    className={`flex items-center justify-between w-full px-4 py-2 text-sm text-left transition-colors ${routeFilter === 'All' ? 'bg-blue-50 text-blue-700 font-medium' : 'text-gray-700 hover:bg-gray-50'}`}
                  >
                    <span>All Units</span>
                    <span className="text-xs bg-gray-100 text-gray-500 px-1.5 py-0.5 rounded-full">{unitsList.length}</span>
                  </button>
                  {MOCK_ROUTES.map(route => {
                    const count = unitsList.filter(u => u.route.toLowerCase() === route.name.toLowerCase()).length;
                    const isActive = routeFilter === route.name;
                    return (
                      <button
                        key={route.id}
                        onClick={() => { setRouteFilter(route.name); setRouteDropdownOpen(false); }}
                        className={`flex items-center justify-between w-full px-4 py-2 text-sm text-left transition-colors ${isActive ? 'bg-blue-50 text-blue-700 font-medium' : 'text-gray-700 hover:bg-gray-50'}`}
                      >
                        <div className="flex items-center gap-2">
                          <div className={`w-2 h-2 rounded-full bg-${route.color}-500`}></div>
                          {route.name}
                        </div>
                        <span className="text-xs bg-gray-100 text-gray-500 px-1.5 py-0.5 rounded-full">{count}</span>
                      </button>
                    )
                  })}
                  <div className="my-1 border-t border-gray-100"></div>
                  <button
                    onClick={() => { setRouteFilter('Unassigned'); setRouteDropdownOpen(false); }}
                    className={`flex items-center justify-between w-full px-4 py-2 text-sm text-left transition-colors ${routeFilter === 'Unassigned' ? 'bg-gray-100 text-gray-900 font-medium' : 'text-gray-700 hover:bg-gray-50'}`}
                  >
                    <div className="flex items-center gap-2">
                      <div className="w-2 h-2 rounded-full bg-gray-400"></div>
                      Unassigned
                    </div>
                    <span className="text-xs bg-gray-100 text-gray-500 px-1.5 py-0.5 rounded-full">
                      {unitsList.filter(u => u.route === 'UNASSIGNED').length}
                    </span>
                  </button>
                </div>
              </>
            )}
          </div>

          {/* Search */}"""

content = content.replace("          {/* Search */}", route_dropdown_html)

# Remove the Route Filter Bar
# Using regex to remove from {/* ROUTE FILTER BAR */} up to the end of the div
import re
content = re.sub(r'\s*\{/\* ROUTE FILTER BAR \*/\}[\s\S]*?</div>\s*\{/\* MAIN CONTENT \*/\}', '\n\n      {/* MAIN CONTENT */}', content)

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "w") as f:
    f.write(content)

