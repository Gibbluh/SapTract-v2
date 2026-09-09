import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# Strip out metricsComponents and chartsComponents entirely
match = re.search(r'const metricsComponents = \{', content)
if match:
    # Find the end by looking for the return statement
    start_idx = match.start()
    return_match = re.search(r'  return \(', content[start_idx:])
    if return_match:
        end_idx = start_idx + return_match.start()
        
        # We also need to fix the sortable state.
        state_match = re.search(r'const \[metricsOrder', content)
        state_start = state_match.start()
        
        # Everything before state_start
        prefix = content[:state_start]
        
        # Now we define the unified state, widgets mapping, and the return
        unified_widgets = """  const [widgetOrder, setWidgetOrder] = useState([
    'metric-revenue', 'metric-active', 'metric-pending', 'metric-users', 'metric-alerts',
    'chart-revenue', 'chart-fleet', 'chart-dispatches'
  ]);

  const sensors = useSensors(
    useSensor(PointerSensor, { activationConstraint: { distance: 5 } }),
    useSensor(KeyboardSensor, { coordinateGetter: sortableKeyboardCoordinates })
  );

  const handleDragEnd = (event) => {
    const { active, over } = event;
    if (!over) return;

    if (active.id !== over.id) {
      setWidgetOrder((items) => {
        const oldIndex = items.indexOf(active.id);
        const newIndex = items.indexOf(over.id);
        return arrayMove(items, oldIndex, newIndex);
      });
    }
  };

  const widgets = {
    'metric-revenue': (
      <SortableItem id="metric-revenue" key="metric-revenue" className="col-span-12 sm:col-span-6 xl:col-span-3 2xl:col-span-2 h-full flex">
        <div className="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm relative overflow-hidden flex flex-col w-full">
          <div className="flex justify-between items-start mb-2">
            <div className="w-10 h-10 bg-blue-50 rounded-lg flex items-center justify-center">
              <TrendingUp className="text-blue-600 w-5 h-5" />
            </div>
            <div className="bg-emerald-100 text-emerald-700 text-[10px] font-bold px-2 py-1 rounded-full flex items-center">
              <ArrowUpRight className="w-3 h-3 mr-1" />
              +12.5%
            </div>
          </div>
          <div className="mt-2">
            <p className="text-xs font-medium text-slate-500 mb-1">Total Revenue Today</p>
            <h2 className="text-2xl sm:text-3xl font-black text-slate-900 tracking-tight">
              {formatCurrency ? formatCurrency(totalRevenue) : `₱124,567`}
            </h2>
          </div>
          <div className="mt-auto pt-4 flex justify-between items-end">
            <p className="text-[11px] text-slate-400">vs ₱110.8k yesterday</p>
            <div className="flex items-end gap-1 opacity-80">
              <div className="w-2 bg-blue-200 rounded-sm h-3"></div>
              <div className="w-2 bg-blue-300 rounded-sm h-4"></div>
              <div className="w-2 bg-blue-400 rounded-sm h-5"></div>
              <div className="w-2 bg-blue-500 rounded-sm h-7"></div>
              <div className="w-2 bg-blue-600 rounded-sm h-8"></div>
            </div>
          </div>
        </div>
      </SortableItem>
    ),
    'metric-active': (
      <SortableItem id="metric-active" key="metric-active" className="col-span-12 sm:col-span-6 xl:col-span-3 2xl:col-span-2 h-full flex">
        <div className="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm flex flex-col w-full">
          <div className="flex justify-between items-start mb-2">
            <div className="w-10 h-10 bg-emerald-50 rounded-lg flex items-center justify-center">
              <Truck className="text-emerald-600 w-5 h-5" />
            </div>
            <div className="bg-emerald-100 text-emerald-700 text-[10px] font-bold px-2 py-1 rounded-full">
              72% Utilization
            </div>
          </div>
          <div className="mt-2">
            <p className="text-xs font-medium text-slate-500 mb-1">Active Fleet</p>
            <h2 className="text-2xl sm:text-3xl font-black text-slate-900 tracking-tight flex items-baseline">
              {totalActive} <span className="text-sm font-medium text-slate-400 ml-1">/25 Units</span>
            </h2>
          </div>
          <div className="mt-auto pt-4">
            <div className="w-full h-2 rounded-full overflow-hidden flex mb-2">
              <div className="bg-emerald-500 h-full" style={{ width: '60%' }}></div>
              <div className="bg-amber-400 h-full" style={{ width: '25%' }}></div>
              <div className="bg-red-500 h-full" style={{ width: '15%' }}></div>
            </div>
            <div className="flex justify-between items-center text-[10px]">
              <div className="flex items-center gap-3">
                <span className="flex items-center text-slate-500"><span className="w-2 h-2 rounded-full bg-emerald-500 mr-1"></span> {good} Good</span>
                <span className="flex items-center text-slate-500"><span className="w-2 h-2 rounded-full bg-amber-400 mr-1"></span> {warn} Warn</span>
              </div>
              <Link to="/units" className="text-emerald-600 font-semibold hover:underline relative z-20">View</Link>
            </div>
          </div>
        </div>
      </SortableItem>
    ),
    'metric-pending': (
      <SortableItem id="metric-pending" key="metric-pending" className="col-span-12 sm:col-span-6 xl:col-span-2 h-full flex">
        <div className="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm flex flex-col w-full">
          <div className="flex justify-between items-start mb-2">
            <div className="w-10 h-10 bg-amber-50 rounded-lg flex items-center justify-center">
              <ClipboardList className="text-amber-500 w-5 h-5" />
            </div>
            <div className="bg-amber-100 text-amber-700 text-[10px] font-bold px-2 py-1 rounded-full flex items-center">
              <span className="w-1.5 h-1.5 rounded-full bg-amber-500 mr-1"></span>
              Urgent
            </div>
          </div>
          <div className="mt-2">
            <p className="text-xs font-medium text-slate-500 mb-1">Pending Actions</p>
            <h2 className="text-2xl sm:text-3xl font-black text-slate-900 tracking-tight flex items-baseline">
              12 <span className="text-sm font-medium text-slate-400 ml-1">tasks</span>
            </h2>
          </div>
          <div className="mt-auto pt-5 flex justify-between items-center">
            <p className="text-[11px] text-slate-500">4 fuel • 5 shift • 3 maint</p>
            <button className="text-amber-600 text-xs font-semibold hover:underline flex items-center relative z-20">
              Review &rarr;
            </button>
          </div>
        </div>
      </SortableItem>
    ),
    'metric-users': (
      <SortableItem id="metric-users" key="metric-users" className="col-span-12 sm:col-span-6 xl:col-span-2 h-full flex">
        <div className="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm flex flex-col w-full">
          <div className="flex justify-between items-start mb-2">
            <div className="w-10 h-10 bg-purple-50 rounded-lg flex items-center justify-center">
              <Users className="text-purple-600 w-5 h-5" />
            </div>
            <div className="bg-purple-100 text-purple-700 text-[10px] font-bold px-2 py-1 rounded-full">
              Live Staff
            </div>
          </div>
          <div className="mt-2">
            <p className="text-xs font-medium text-slate-500 mb-1">Users Online</p>
            <h2 className="text-2xl sm:text-3xl font-black text-slate-900 tracking-tight flex items-baseline">
              5 <span className="text-sm font-medium text-slate-400 ml-1">Active Now</span>
            </h2>
          </div>
          <div className="mt-auto pt-5 flex justify-between items-center">
            <div className="flex -space-x-2">
              <div className="w-6 h-6 rounded-full bg-blue-500 border border-white flex items-center justify-center text-[9px] text-white font-bold">DI</div>
              <div className="w-6 h-6 rounded-full bg-purple-500 border border-white flex items-center justify-center text-[9px] text-white font-bold">M</div>
              <div className="w-6 h-6 rounded-full bg-amber-500 border border-white flex items-center justify-center text-[9px] text-white font-bold">ES</div>
            </div>
            <Link to="/users" className="text-purple-600 text-xs font-semibold hover:underline relative z-20">
              Roster
            </Link>
          </div>
        </div>
      </SortableItem>
    ),
    'metric-alerts': (
      <SortableItem id="metric-alerts" key="metric-alerts" className="col-span-12 sm:col-span-6 xl:col-span-2 h-full flex">
        <div className="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm flex flex-col w-full">
          <div className="flex justify-between items-start mb-2">
            <div className="w-10 h-10 bg-red-50 rounded-lg flex items-center justify-center">
              <ShieldAlert className="text-red-500 w-5 h-5" />
            </div>
            <div className="bg-red-100 text-red-700 text-[10px] font-bold px-2 py-1 rounded-full">
              Action Needed
            </div>
          </div>
          <div className="mt-2">
            <p className="text-xs font-medium text-slate-500 mb-1">System Alerts</p>
            <h2 className="text-2xl sm:text-3xl font-black text-slate-900 tracking-tight flex items-baseline">
              3 <span className="text-sm font-medium text-slate-400 ml-1">Open Issues</span>
            </h2>
          </div>
          <div className="mt-auto pt-5 flex justify-between items-center">
            <div className="flex gap-2">
              <span className="bg-red-100 text-red-700 text-[10px] px-1.5 py-0.5 rounded font-semibold">1 Crit</span>
              <span className="bg-amber-100 text-amber-700 text-[10px] px-1.5 py-0.5 rounded font-semibold">2 Warn</span>
            </div>
            <button className="text-slate-500 text-xs hover:underline decoration-slate-400 underline-offset-2 relative z-20">
              Dismiss
            </button>
          </div>
        </div>
      </SortableItem>
    ),
    'chart-revenue': (
      <SortableItem id="chart-revenue" key="chart-revenue" className="col-span-12 lg:col-span-8 flex h-full">
        <div className="bg-white border border-slate-200 rounded-3xl p-6 shadow-sm flex flex-col w-full h-full">
          <div className="flex justify-between items-center mb-1">
            <div className="flex items-center gap-3">
              <h2 className="text-lg sm:text-xl font-bold text-slate-900">Revenue Overview</h2>
              <span className="bg-blue-50 text-blue-600 text-xs font-semibold px-2.5 py-0.5 rounded-full border border-blue-100">Live Feed</span>
            </div>
            <div className="flex bg-slate-50 rounded-lg p-1 border border-slate-200 relative z-20">
              <button className="px-3 py-1 text-xs font-bold bg-white text-blue-600 rounded shadow-sm border border-slate-200">Today</button>
              <button className="px-3 py-1 text-xs font-medium text-slate-500 hover:text-slate-700">Week</button>
              <button className="px-3 py-1 text-xs font-medium text-slate-500 hover:text-slate-700">Month</button>
            </div>
          </div>
          <p className="text-xs text-slate-500 mb-8">Real-time gross passenger fares & collection analytics</p>
          
          <div className="relative h-64 w-full mb-6 relative z-10">
            <div className="absolute top-0 left-0 flex items-center text-slate-400 text-xs">
              <Info className="w-3.5 h-3.5 mr-1" />
              Hover across timeline curve for interval revenue breakdown
            </div>
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={mockRevenueData} margin={{ top: 30, right: 10, left: -20, bottom: 0 }}>
                <defs>
                  <linearGradient id="colorRevenue" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.3}/>
                    <stop offset="95%" stopColor="#3b82f6" stopOpacity={0}/>
                  </linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#f1f5f9" />
                <XAxis dataKey="time" axisLine={false} tickLine={false} tick={{ fontSize: 10, fill: '#64748b' }} dy={10} />
                <YAxis axisLine={false} tickLine={false} tick={{ fontSize: 10, fill: '#64748b' }} tickFormatter={(val) => `₱${val/1000}k`} />
                <Tooltip 
                  contentStyle={{ borderRadius: '12px', border: 'none', boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)' }}
                  formatter={(value) => [`₱${value.toLocaleString()}`, 'Revenue']}
                />
                <Area type="monotone" dataKey="value" stroke="#3b82f6" strokeWidth={3} fillOpacity={1} fill="url(#colorRevenue)" dot={{ stroke: '#3b82f6', strokeWidth: 2, fill: '#fff', r: 4 }} activeDot={{ r: 6, strokeWidth: 0, fill: '#2563eb' }} />
              </AreaChart>
            </ResponsiveContainer>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mt-auto border-t border-slate-100 pt-5">
            <div className="flex items-center gap-3 bg-slate-50/50 rounded-xl p-3 border border-slate-100">
              <div className="w-10 h-10 bg-blue-50 text-blue-500 rounded-lg flex items-center justify-center shrink-0">
                <TrendingUp className="w-5 h-5" />
              </div>
              <div>
                <p className="text-[10px] text-slate-500 font-medium">Average Per Trip</p>
                <p className="text-base font-bold text-slate-900 flex items-baseline gap-1">
                  ₱384 <span className="text-[10px] text-emerald-500">+5.4%</span>
                </p>
              </div>
            </div>
            
            <div className="flex items-center gap-3 bg-slate-50/50 rounded-xl p-3 border border-slate-100">
              <div className="w-10 h-10 bg-emerald-50 text-emerald-500 rounded-lg flex items-center justify-center shrink-0">
                <Activity className="w-5 h-5" />
              </div>
              <div>
                <p className="text-[10px] text-slate-500 font-medium">Total Trips Completed</p>
                <p className="text-base font-bold text-slate-900 flex items-baseline gap-1">
                  324 <span className="text-[10px] text-slate-400 font-normal">dispatches</span>
                </p>
              </div>
            </div>

            <div className="flex items-center gap-3 bg-slate-50/50 rounded-xl p-3 border border-slate-100">
              <div className="w-10 h-10 bg-amber-50 text-amber-500 rounded-lg flex items-center justify-center shrink-0">
                <Fuel className="w-5 h-5" />
              </div>
              <div>
                <p className="text-[10px] text-slate-500 font-medium">Fuel Efficiency</p>
                <p className="text-base font-bold text-slate-900 flex items-baseline gap-1">
                  4.2 km/L <span className="text-[9px] font-bold text-emerald-600 bg-emerald-100 px-1 py-0.5 rounded">Euro-4 OK</span>
                </p>
              </div>
            </div>
          </div>
        </div>
      </SortableItem>
    ),
    'chart-fleet': (
      <SortableItem id="chart-fleet" key="chart-fleet" className="col-span-12 lg:col-span-4 flex h-full">
        <div className="bg-white border border-slate-200 rounded-3xl p-6 shadow-sm flex flex-col items-center w-full h-full">
          <div className="w-full flex justify-between items-center mb-6">
            <h2 className="text-lg font-bold text-slate-900 flex items-center gap-1">
              Fleet Health Score <Info className="w-3.5 h-3.5 text-slate-400" />
            </h2>
            <span className="bg-emerald-50 text-emerald-600 text-xs font-semibold px-2.5 py-0.5 rounded-full border border-emerald-100">Good Standby</span>
          </div>
          
          <div className="relative w-48 h-48 mb-4">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={pieData}
                  cx="50%"
                  cy="50%"
                  innerRadius={70}
                  outerRadius={90}
                  paddingAngle={2}
                  dataKey="value"
                  stroke="none"
                  cornerRadius={4}
                >
                  {pieData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                  ))}
                </Pie>
              </PieChart>
            </ResponsiveContainer>
            <div className="absolute inset-0 flex flex-col items-center justify-center pointer-events-none">
              <span className="text-3xl font-black text-slate-900">85%</span>
              <span className="text-[9px] font-bold text-slate-500 tracking-wider">FLEET INDEX</span>
            </div>
          </div>

          <p className="text-[11px] text-slate-500 text-center mb-6 px-4">
            20 of 25 Modern PUVs road-ready for peak commute
          </p>

          <div className="w-full grid grid-cols-2 gap-3 mb-6">
            <div className="bg-emerald-50/50 border border-emerald-100 rounded-lg p-2.5 flex justify-between items-center">
              <div className="flex items-center text-xs font-medium text-slate-700">
                <div className="w-2 h-2 rounded-full bg-emerald-500 mr-2"></div>
                Good
              </div>
              <span className="text-xs font-bold text-emerald-700">{good} units</span>
            </div>
            
            <div className="bg-amber-50/50 border border-amber-100 rounded-lg p-2.5 flex justify-between items-center">
              <div className="flex items-center text-xs font-medium text-slate-700">
                <div className="w-2 h-2 rounded-full bg-amber-500 mr-2"></div>
                Warning
              </div>
              <span className="text-xs font-bold text-amber-700">{warn} units</span>
            </div>

            <div className="bg-red-50/50 border border-red-100 rounded-lg p-2.5 flex justify-between items-center">
              <div className="flex items-center text-xs font-medium text-slate-700">
                <div className="w-2 h-2 rounded-full bg-red-500 mr-2"></div>
                Critical
              </div>
              <span className="text-xs font-bold text-red-700">{crit} units</span>
            </div>

            <div className="bg-slate-50 border border-slate-200 rounded-lg p-2.5 flex justify-between items-center">
              <div className="flex items-center text-xs font-medium text-slate-700">
                <div className="w-2 h-2 rounded-full bg-slate-400 mr-2"></div>
                Idle
              </div>
              <span className="text-xs font-bold text-slate-600">{idle} units</span>
            </div>
          </div>

          <Link to="/maintenance" className="w-full mt-auto bg-slate-50 hover:bg-slate-100 text-slate-700 text-xs font-bold py-3 rounded-xl flex items-center justify-center border border-slate-200 transition-colors relative z-20">
            View Fleet Report <span className="ml-1">&gt;</span>
          </Link>
        </div>
      </SortableItem>
    ),
    'chart-dispatches': (
      <SortableItem id="chart-dispatches" key="chart-dispatches" className="col-span-12 lg:col-span-4 flex h-full">
        <div className="bg-white border border-slate-200 rounded-3xl p-6 shadow-sm flex flex-col w-full h-full">
          <div className="flex justify-between items-center mb-4">
            <h2 className="text-lg font-bold text-slate-900 flex items-center gap-2">
              <Activity className="w-5 h-5 text-blue-500" />
              Active Dispatches
            </h2>
          </div>
          
          <div className="flex flex-col gap-3 overflow-y-auto pr-1 relative z-20" style={{ maxHeight: '350px' }}>
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
      </SortableItem>
    )
  };

  return (
    <DndContext sensors={sensors} collisionDetection={closestCenter} onDragEnd={handleDragEnd}>
      <div className="space-y-6">
        <SortableContext items={widgetOrder} strategy={rectSortingStrategy}>
          <div className="grid grid-cols-12 gap-5 grid-flow-row-dense">
            {widgetOrder.map(id => widgets[id])}
          </div>
        </SortableContext>
      </div>
    </DndContext>
  );
"""

        new_content = prefix + unified_widgets + "\n};\n\nexport default SuperAdminDashboard;\n"
        with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
            f.write(new_content)
        print("Success")
    else:
        print("Could not find return_match")
else:
    print("Could not find metricsComponents")

