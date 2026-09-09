import re

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

# Add Map and Plus to imports if needed
content = content.replace("Search, Plus, X,", "Search, Plus, X, Map, Settings2,")

# 1. Add MOCK_ROUTES after MOCK_UNITS
mock_routes = """
const MOCK_ROUTES = [
  { id: 'RT-01', name: 'Langgam', color: 'blue', units: 12, description: 'Langgam to Complex', status: 'Active' },
  { id: 'RT-02', name: 'Villarosa', color: 'emerald', units: 8, description: 'Villarosa to Complex', status: 'Active' },
  { id: 'RT-03', name: 'Bayan-Bayanan', color: 'purple', units: 10, description: 'Bayan-Bayanan to Complex', status: 'Active' },
  { id: 'RT-04', name: 'Estrella', color: 'orange', units: 7, description: 'Estrella to Complex', status: 'Active' },
  { id: 'RT-05', name: 'Calamba', color: 'red', units: 5, description: 'Calamba to Complex', status: 'Active' },
];
"""
content = re.sub(r'(const UnitManagementPage = \(\) => {)', mock_routes + r'\n\1', content)

# 2. Add route state
route_states = """  const [routeFilter, setRouteFilter] = useState('All');
  const [routeModalOpen, setRouteModalOpen] = useState(false);"""
content = content.replace("const [statusFilter, setStatusFilter] = useState('All');", "const [statusFilter, setStatusFilter] = useState('All');\n" + route_states)


# 3. Update filteredUnits logic
filtered_units_logic = """  const filteredUnits = useMemo(() => {
    return unitsList.filter(unit => {
      const matchesSearch = unit.plateNumber.toLowerCase().includes(searchQuery.toLowerCase()) || 
                            unit.bodyNumber.toLowerCase().includes(searchQuery.toLowerCase());
      const matchesStatus = statusFilter === 'All' || unit.status === statusFilter;
      const matchesRoute = routeFilter === 'All' || 
                           (routeFilter === 'Unassigned' && unit.route === 'UNASSIGNED') || 
                           (unit.route.toLowerCase() === routeFilter.toLowerCase());
      return matchesSearch && matchesStatus && matchesRoute;
    });
  }, [unitsList, searchQuery, statusFilter, routeFilter]);"""

content = re.sub(r'const filteredUnits = useMemo\(\(\) => \{[\s\S]*?\}, \[unitsList, searchQuery, statusFilter\]\);', filtered_units_logic, content)

# 4. Route Filter Bar
route_filter_bar = """
      {/* ROUTE FILTER BAR */}
      <div className="bg-white border-b border-gray-200 px-6 py-3 flex gap-3 overflow-x-auto shrink-0 hide-scrollbar">
        <button
          onClick={() => setRouteFilter('All')}
          className={`flex items-center gap-2 px-4 py-1.5 rounded-full border-2 text-sm font-medium transition-all whitespace-nowrap
            ${routeFilter === 'All' ? 'border-gray-900 bg-gray-900 text-white shadow-md' : 'border-gray-200 text-gray-600 hover:border-gray-300'}`}
        >
          All Units <span className={`px-1.5 py-0.5 rounded-full text-[10px] ${routeFilter === 'All' ? 'bg-white/20 text-white' : 'bg-gray-100 text-gray-500'}`}>{unitsList.length}</span>
        </button>
        
        {MOCK_ROUTES.map(route => {
          const isActive = routeFilter === route.name;
          const routeColorMap = {
            'blue': 'border-blue-500 bg-blue-50 text-blue-700 hover:border-blue-600',
            'emerald': 'border-emerald-500 bg-emerald-50 text-emerald-700 hover:border-emerald-600',
            'purple': 'border-purple-500 bg-purple-50 text-purple-700 hover:border-purple-600',
            'orange': 'border-orange-500 bg-orange-50 text-orange-700 hover:border-orange-600',
            'red': 'border-red-500 bg-red-50 text-red-700 hover:border-red-600'
          };
          const activeStyle = routeColorMap[route.color] || 'border-gray-900 bg-gray-900 text-white';
          const count = unitsList.filter(u => u.route.toLowerCase() === route.name.toLowerCase()).length;
          
          return (
            <button
              key={route.id}
              onClick={() => setRouteFilter(route.name)}
              className={`flex items-center gap-2 px-4 py-1.5 rounded-full border-2 text-sm font-medium transition-all whitespace-nowrap
                ${isActive ? activeStyle + ' shadow-sm' : 'border-gray-200 text-gray-600 hover:border-gray-300'}`}
            >
              <div className={`w-2 h-2 rounded-full ${isActive ? 'bg-current' : `bg-${route.color}-500`}`}></div>
              {route.name}
              <span className={`px-1.5 py-0.5 rounded-full text-[10px] ${isActive ? 'bg-black/10' : 'bg-gray-100 text-gray-500'}`}>{count}</span>
            </button>
          );
        })}
        
        <button
          onClick={() => setRouteFilter('Unassigned')}
          className={`flex items-center gap-2 px-4 py-1.5 rounded-full border-2 text-sm font-medium transition-all whitespace-nowrap
            ${routeFilter === 'Unassigned' ? 'border-gray-600 bg-gray-600 text-white shadow-sm' : 'border-gray-200 text-gray-600 hover:border-gray-300'}`}
        >
          <div className={`w-2 h-2 rounded-full ${routeFilter === 'Unassigned' ? 'bg-white' : 'bg-gray-400'}`}></div>
          Unassigned
          <span className={`px-1.5 py-0.5 rounded-full text-[10px] ${routeFilter === 'Unassigned' ? 'bg-white/20' : 'bg-gray-100 text-gray-500'}`}>
            {unitsList.filter(u => u.route === 'UNASSIGNED').length}
          </span>
        </button>
      </div>
"""
content = content.replace("</header>\n\n      {/* MAIN CONTENT */}", "</header>\n" + route_filter_bar + "\n      {/* MAIN CONTENT */}")

# 5. Route Summary Card
route_summary = """
        {/* Route Summary Card */}
        {routeFilter !== 'All' && routeFilter !== 'Unassigned' && (
          <div className="bg-white rounded-xl border border-gray-200 shadow-sm p-5 mb-6 flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div>
              <div className="flex items-center gap-3 mb-1">
                <h2 className="text-xl font-bold text-gray-900">{routeFilter} Route</h2>
                <span className="bg-green-100 text-green-700 text-[10px] font-bold px-2 py-0.5 rounded uppercase tracking-wider">Active</span>
              </div>
              <div className="flex flex-wrap items-center gap-4 text-sm text-gray-600">
                <div className="flex items-center gap-1.5"><Truck className="w-4 h-4 text-gray-400" /> <span className="font-semibold text-gray-900">{filteredUnits.length}</span> Total Units</div>
                <div className="w-1 h-1 rounded-full bg-gray-300 hidden md:block"></div>
                <div className="flex items-center gap-3">
                  <span className="flex items-center gap-1.5"><div className="w-2 h-2 rounded-full bg-emerald-500"></div> {filteredUnits.filter(u=>u.status==='Available').length} Available</span>
                  <span className="flex items-center gap-1.5"><div className="w-2 h-2 rounded-full bg-amber-500"></div> {filteredUnits.filter(u=>u.status==='In Maintenance').length} Maintenance</span>
                </div>
              </div>
            </div>
            <div className="flex gap-2">
               <button className="px-4 py-2 bg-white border border-gray-200 text-gray-700 rounded-lg text-sm font-medium hover:bg-gray-50 transition-colors shadow-sm flex items-center gap-2">
                 <Settings2 className="w-4 h-4" /> Manage Route
               </button>
               <button className="px-4 py-2 bg-blue-50 text-blue-700 rounded-lg text-sm font-medium hover:bg-blue-100 transition-colors flex items-center gap-2">
                 <Map className="w-4 h-4" /> View Schedule
               </button>
            </div>
          </div>
        )}
        
        {routeFilter === 'Unassigned' && (
          <div className="bg-gray-100 rounded-xl border border-gray-200 border-dashed p-6 mb-6 flex items-center justify-between">
             <div>
                <h2 className="text-lg font-bold text-gray-900 mb-1">Unassigned Units</h2>
                <p className="text-sm text-gray-500">These units are not currently assigned to any active route.</p>
             </div>
             <button className="px-4 py-2 bg-white border border-gray-200 text-gray-700 rounded-lg text-sm font-medium hover:bg-gray-50 transition-colors shadow-sm flex items-center gap-2">
                 Assign Units
             </button>
          </div>
        )}
"""

content = content.replace("        {viewMode === 'grid' ? (", route_summary + "\n        {viewMode === 'grid' ? (")

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "w") as f:
    f.write(content)
