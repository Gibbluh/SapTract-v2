import re

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

status_dropdown = """          {/* Status Dropdown Filter */}
          <div className="relative">
            <button
              onClick={() => setStatusDropdownOpen(!statusDropdownOpen)}
              className="px-4 py-2 bg-white border border-gray-300 rounded-lg text-sm font-medium text-gray-700 hover:bg-gray-50 flex items-center gap-2 transition-colors"
            >
              Status: {statusFilter}
              <span className="bg-gray-100 text-gray-600 px-1.5 py-0.5 rounded-full text-[10px] font-bold ml-1">
                {statusFilter === 'All' ? unitsList.length : unitsList.filter(u => u.status === statusFilter).length}
              </span>
              <ChevronDown className="w-4 h-4 text-gray-400" />
            </button>
            
            {statusDropdownOpen && (
              <>
                <div className="fixed inset-0 z-40" onClick={() => setStatusDropdownOpen(false)}></div>
                <div className="absolute top-full mt-2 left-0 sm:right-0 sm:left-auto w-56 bg-white border border-gray-200 rounded-xl shadow-lg z-50 py-1 flex flex-col">
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
          </div>"""

content = re.sub(r'\{\/\* Status Filter \*\/\}.*?<\/div>', status_dropdown, content, flags=re.DOTALL)

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "w") as f:
    f.write(content)
