import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

mock_dispatches = """
const MOCK_DISPATCHES = [
  { id: 1, name: "Juan Dela Cruz", vehicle: "NGQ 3326", route: "Cubao - Antipolo", avatar: "https://i.pravatar.cc/150?u=1" },
  { id: 2, name: "Pedro Penduko", vehicle: "UVP 9182", route: "Makati - BGC", avatar: "https://i.pravatar.cc/150?u=2" },
  { id: 3, name: "Cardo Dalisay", vehicle: "XYZ 1234", route: "Pasay - MOA", avatar: "https://i.pravatar.cc/150?u=3" },
  { id: 4, name: "Lito Lapid", vehicle: "DEF 5678", route: "Quezon Ave - UP", avatar: "https://i.pravatar.cc/150?u=4" }
];
"""
if 'MOCK_DISPATCHES' not in content:
    content = content.replace('const mockRevenueData = [', mock_dispatches + '\nconst mockRevenueData = [')

# Now wrap the Right column in a div
right_col_start = r'        {/\* Right: Fleet Health Score \*/}\s*<div className="bg-white border border-slate-200 rounded-3xl p-6 shadow-sm flex flex-col items-center">'
right_col_replacement = """        {/* Right Column */}
        <div className="flex flex-col gap-6">
          {/* Fleet Health Score */}
          <div className="bg-white border border-slate-200 rounded-3xl p-6 shadow-sm flex flex-col items-center">"""

content = re.sub(right_col_start, right_col_replacement, content)

# Now find where the fleet health score ends
# It ends at </Link>\n        </div>
# I'll replace it with:
end_fleet = r'            View Fleet Report & Diagnostics <span className="ml-1">&gt;</span>\s*</Link>\s*</div>'

dispatch_ui = """            View Fleet Report & Diagnostics <span className="ml-1">&gt;</span>
          </Link>
        </div>

        {/* Active Dispatch */}
        <div className="bg-white border border-slate-200 rounded-3xl p-6 shadow-sm flex flex-col flex-1">
          <div className="flex justify-between items-center mb-4">
            <h2 className="text-lg font-bold text-slate-900 flex items-center gap-2">
              <Activity className="w-5 h-5 text-blue-500" />
              Active Dispatches
            </h2>
          </div>
          
          <div className="flex flex-col gap-3 overflow-y-auto pr-1" style={{ maxHeight: '350px' }}>
            {MOCK_DISPATCHES.map((driver) => (
              <div key={driver.id} className="flex items-center p-3 rounded-2xl border border-slate-100 bg-slate-50 hover:bg-slate-100 hover:border-slate-200 transition-colors cursor-pointer">
                <img src={driver.avatar} alt={driver.name} className="w-12 h-12 rounded-full border-2 border-white shadow-sm mr-4" />
                <div className="flex-1 min-w-0">
                  <h4 className="text-sm font-bold text-slate-900 truncate">{driver.name}</h4>
                  <p className="text-[11px] font-medium text-slate-500 truncate flex items-center gap-1 mt-0.5">
                    <Truck className="w-3 h-3 text-slate-400" /> {driver.vehicle}
                  </p>
                  <p className="text-[10px] font-semibold text-blue-600 truncate mt-1 bg-blue-50 px-2 py-0.5 rounded-full inline-block">
                    {driver.route}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>"""

content = re.sub(end_fleet, dispatch_ui, content)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
