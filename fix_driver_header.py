import re

with open("frontend/src/pages/admin/DriverManagementPage.jsx", "r") as f:
    content = f.read()

# I will find the whole block from <header className="sticky top-0 z-20...> to the end of the search input

header_start_index = content.find('<header className="sticky top-0 z-20 bg-white border-b border-slate-200 px-6 pt-4 pb-0">')
if header_start_index == -1:
    print("Header start not found")

table_start_index = content.find('          {/* TABLE */}')
if table_start_index == -1:
    print("Table start not found")

old_block = content[header_start_index:table_start_index]

new_block = """
        {/* Page Header */}
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6 px-6 pt-6">
          <div>
            <div className="flex items-center gap-1.5 text-[11px] font-medium text-slate-500 mb-1">
              <span>SPTC</span>
              <span className="opacity-50">/</span>
              <span>Fleet Personnel</span>
              <span className="opacity-50">/</span>
              <span className="font-semibold text-slate-700">Drivers</span>
            </div>
            <h1 className="text-2xl font-bold text-slate-900 tracking-tight">Driver Management</h1>
          </div>
          <div className="flex items-center gap-2">
            <button className="flex items-center gap-2 px-3 py-2 border border-slate-300 rounded-lg text-sm font-medium text-slate-700 hover:bg-slate-50 transition-colors bg-white shadow-sm">
              <Upload className="w-4 h-4" />
              <span className="hidden sm:inline">Import</span>
            </button>
            <button className="flex items-center gap-2 px-3 py-2 border border-slate-300 rounded-lg text-sm font-medium text-slate-700 hover:bg-slate-50 transition-colors bg-white shadow-sm">
              <Download className="w-4 h-4" />
              <span className="hidden sm:inline">Export</span>
            </button>
            <button 
              onClick={() => setFormOpen(true)}
              className="px-4 py-2 bg-blue-600 text-white rounded-lg text-sm font-bold hover:bg-blue-700 transition-colors shadow-sm flex items-center gap-2 whitespace-nowrap"
            >
              <Plus className="w-4 h-4" /> Add Driver
            </button>
          </div>
        </div>

      {/* MAIN CONTENT */}
      <main className="flex-1 px-6 pb-6 flex flex-col relative">
        
        {/* Filters Toolbar Card */}
        <div className="bg-white border border-gray-200 rounded-xl p-2.5 shadow-sm flex flex-col lg:flex-row items-stretch lg:items-center gap-3 mb-6">
          
          <div className="flex items-center gap-2 w-full lg:w-auto shrink-0 flex-wrap">
            {/* Search Input */}
            <div className="relative flex-1 sm:max-w-xs">
              <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" />
              <input 
                type="text" 
                placeholder="Search drivers..." 
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="bg-white text-gray-900 placeholder-gray-400 pl-9 pr-4 py-2 border border-gray-300 rounded-lg text-sm w-full focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-shadow shadow-sm"
              />
            </div>

            {/* Status Dropdown Filter */}
            <div className="relative">
              <button
                onClick={() => {
                  const el = document.getElementById('status-dropdown-drivers');
                  if (el) el.classList.toggle('hidden');
                }}
                className="px-4 py-2 bg-white border border-gray-300 rounded-lg text-sm font-medium text-gray-700 hover:bg-gray-50 flex items-center gap-2 transition-colors whitespace-nowrap"
              >
                <Filter className="w-4 h-4 text-gray-400" />
                Status: {activeTab}
                <ChevronDown className="w-4 h-4 text-gray-400 ml-1" />
              </button>
              
              <div id="status-dropdown-drivers" className="hidden absolute top-full mt-2 left-0 w-56 bg-white border border-gray-200 rounded-xl shadow-lg z-50 py-1 flex flex-col">
                <div className="px-3 py-2 text-xs font-semibold text-gray-500 uppercase tracking-wider border-b border-gray-100">
                  Filter by Status
                </div>
                {['All Drivers', 'Active', 'Suspended', 'Inactive', 'Documents Expiring'].map(tab => {
                  const isActive = activeTab === tab;
                  let dotColor = 'bg-gray-400';
                  if (tab === 'Active') dotColor = 'bg-emerald-500';
                  if (tab === 'Suspended') dotColor = 'bg-red-500';
                  if (tab === 'Documents Expiring') dotColor = 'bg-amber-500';
                  return (
                    <button
                      key={tab}
                      onClick={() => { 
                        setActiveTab(tab); 
                        setPage(1); 
                        const el = document.getElementById('status-dropdown-drivers');
                        if (el) el.classList.add('hidden');
                      }}
                      className={`flex items-center justify-between w-full px-4 py-2 text-sm text-left transition-colors ${isActive ? 'bg-blue-50 text-blue-700 font-medium' : 'text-gray-700 hover:bg-gray-50'}`}
                    >
                      <div className="flex items-center gap-2">
                        {tab !== 'All Drivers' && <div className={`w-2 h-2 rounded-full ${dotColor}`}></div>}
                        {tab}
                      </div>
                    </button>
                  )
                })}
              </div>
            </div>
          </div>
          
          <div className="flex items-center gap-3 shrink-0 lg:ml-auto">
             <div className="text-sm text-slate-500 font-medium px-2">
                Showing {(page - 1) * rowsPerPage + 1}-{Math.min(page * rowsPerPage, filteredDrivers.length)} of {filteredDrivers.length}
             </div>
          </div>
        </div>

        <div className="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden flex flex-col flex-1">
"""

if header_start_index != -1 and table_start_index != -1:
    # Also I need to add ChevronDown and Filter to lucide-react imports if they aren't there
    content = content.replace(old_block, new_block)

with open("frontend/src/pages/admin/DriverManagementPage.jsx", "w") as f:
    f.write(content)
print("Done.")
