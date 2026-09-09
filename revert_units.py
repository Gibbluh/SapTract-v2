import re

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

# 1. Remove + Add Unit from Page Header
header_pattern = r'<div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6">\s*<div>\s*<div className="flex items-center gap-1.5 text-\[11px\] font-medium text-slate-500 mb-1">\s*<span>SPTC</span>\s*<span className="opacity-50">/</span>\s*<span>Fleet Vehicles</span>\s*<span className="opacity-50">/</span>\s*<span className="font-semibold text-slate-700">Modern Jeepneys</span>\s*</div>\s*<h1 className="text-2xl font-bold text-slate-900 tracking-tight">Unit Management</h1>\s*</div>\s*<button[^>]*>\s*<Plus className="w-4 h-4" /> Add Unit\s*</button>\s*</div>'

new_header = """<div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6">
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
        </div>"""

if re.search(header_pattern, content):
    content = re.sub(header_pattern, new_header, content)
else:
    print("Header not found exactly.")
    # Try a looser match
    loose_pattern = r'<button[^>]*>\s*<Plus className="w-4 h-4" /> Add Unit\s*</button>'
    # Only replace the first occurrence (which is in the header)
    content = content.replace('<button \n            onClick={() => setFormOpen(true)}\n            className="px-5 py-2.5 bg-blue-600 text-white rounded-lg text-sm font-bold hover:bg-blue-700 transition-colors shadow-sm flex items-center gap-2 whitespace-nowrap"\n          >\n            <Plus className="w-4 h-4" /> Add Unit\n          </button>', '')


# 2. Re-arrange Filters Toolbar Card
filter_start = content.find('{/* Filters Toolbar Card */}')
filter_end = content.find('{/* Main Content Area */}')

if filter_start != -1 and filter_end != -1:
    old_filter = content[filter_start:filter_end]
    
    # We will rebuild the filter bar
    # We need to extract the Dropdowns (Status and Route) and Search Input, and the Grid/List toggle.
    
    new_filter = """{/* Filters Toolbar Card */}
        <div className="flex flex-wrap items-center gap-3 mb-6">
          {/* Status Dropdown Filter */}
          <div className="relative shrink-0">
            <button
              onClick={() => setStatusDropdownOpen(!statusDropdownOpen)}
              className="px-4 py-2 bg-white border border-gray-300 rounded-lg text-sm font-medium text-gray-700 hover:bg-gray-50 flex items-center gap-2 transition-colors"
            >
              Status: {statusFilter}
              <ChevronDown className="w-4 h-4 text-gray-400 ml-1" />
            </button>
            
            {statusDropdownOpen && (
              <>
                <div className="fixed inset-0 z-40" onClick={() => setStatusDropdownOpen(false)}></div>
                <div className="absolute top-full mt-2 left-0 w-56 bg-white border border-gray-200 rounded-xl shadow-lg z-50 py-1 flex flex-col">
                  <div className="px-3 py-2 text-xs font-semibold text-gray-500 uppercase tracking-wider border-b border-gray-100">
                    Filter by Status
                  </div>
                  {['All', 'Available', 'In Maintenance', 'Out of Service'].map(status => {
                    const count = status === 'All' ? unitsList.length : unitsList.filter(u => u.status === status).length;
                    const isActive = statusFilter === status;
                    
                    let dotColor = 'bg-gray-400';
                    if (status === 'Available') dotColor = 'bg-emerald-500';
                    if (status === 'In Maintenance') dotColor = 'bg-amber-500';
                    if (status === 'Out of Service') dotColor = 'bg-red-500';

                    return (
                      <button
                        key={status}
                        onClick={() => { setStatusFilter(status); setStatusDropdownOpen(false); }}
                        className={`flex items-center justify-between w-full px-4 py-2 text-sm text-left transition-colors ${isActive ? 'bg-blue-50 text-blue-700 font-medium' : 'text-gray-700 hover:bg-gray-50'}`}
                      >
                        <div className="flex items-center gap-2">
                          {status !== 'All' && <div className={`w-2 h-2 rounded-full ${dotColor}`}></div>}
                          {status === 'All' ? 'All Statuses' : status}
                        </div>
                        <span className="text-xs bg-gray-100 text-gray-500 px-1.5 py-0.5 rounded-full">{count}</span>
                      </button>
                    )
                  })}
                </div>
              </>
            )}
          </div>

          {/* Route Dropdown Filter */}
          <div className="relative shrink-0">
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
                <div className="absolute top-full mt-2 left-0 w-56 bg-white border border-gray-200 rounded-xl shadow-lg z-50 py-1 flex flex-col">
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
                          <div className={`w-2 h-2 rounded-full ${
                            route.color === 'blue' ? 'bg-blue-500' : 
                            route.color === 'emerald' ? 'bg-emerald-500' :
                            route.color === 'purple' ? 'bg-purple-500' :
                            route.color === 'orange' ? 'bg-orange-500' :
                            route.color === 'red' ? 'bg-red-500' : 'bg-gray-500'
                          }`}></div>
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
                    <span className="text-xs bg-gray-100 text-gray-500 px-1.5 py-0.5 rounded-full">{unitsList.filter(u => u.route === 'Unassigned').length}</span>
                  </button>
                </div>
              </>
            )}
          </div>

          {/* Search Input */}
          <div className="relative flex-1 sm:max-w-xs shrink-0">
            <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" />
            <input 
              type="text" 
              placeholder="Search plate, unit..." 
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="bg-white text-gray-900 placeholder-gray-400 pl-9 pr-4 py-2 border border-gray-300 rounded-lg text-sm w-full focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-shadow"
            />
          </div>
          
          <div className="flex-1"></div>

          {/* Grid/List Toggle */}
          <div className="flex items-center bg-gray-100 rounded-lg p-1 shrink-0">
            <button 
              onClick={() => setViewMode('grid')}
              className={`p-1.5 rounded-md transition-colors ${viewMode === 'grid' ? 'bg-white shadow-sm text-blue-600' : 'text-gray-500 hover:text-gray-700'}`}
            >
              <LayoutGrid className="w-4 h-4" />
            </button>
            <button 
              onClick={() => setViewMode('list')}
              className={`p-1.5 rounded-md transition-colors ${viewMode === 'list' ? 'bg-white shadow-sm text-blue-600' : 'text-gray-500 hover:text-gray-700'}`}
            >
              <List className="w-4 h-4" />
            </button>
          </div>

          <button 
            onClick={() => setFormOpen(true)}
            className="px-5 py-2 bg-blue-600 text-white rounded-lg text-sm font-bold hover:bg-blue-700 transition-colors flex items-center gap-2 whitespace-nowrap shrink-0 shadow-sm"
          >
            <Plus className="w-4 h-4" /> Add Unit
          </button>
        </div>

        """
    content = content.replace(old_filter, new_filter)

# 3. Change checkbox styling
content = content.replace('className="checkbox checkbox-sm checkbox-primary rounded border-gray-300"', 'className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 cursor-pointer"')

# 4. Adjust checkbox spacing on list view
content = content.replace('<th className="pl-5 pr-2 py-3 w-10">', '<th className="pl-4 pr-2 py-3 w-10">')
content = content.replace('<td className="pl-5 pr-2 py-3"', '<td className="pl-4 pr-2 py-3"')


with open("frontend/src/pages/admin/UnitManagementPage.jsx", "w") as f:
    f.write(content)
