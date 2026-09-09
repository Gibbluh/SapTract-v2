import re

with open("frontend/src/pages/SuperAdminDashboard.jsx", "r") as f:
    content = f.read()

# 1. Update imports
imports_pattern = r'from "recharts";'
new_imports = "  ComposedChart,\n  Line,\n  Legend,\nfrom \"recharts\";"
content = content.replace(imports_pattern, new_imports)

# 2. Add to WIDGET_CLASSES
widget_classes_pattern = r"'metric-fuel': 'sm:col-span-5 lg:col-span-5 flex h-full',"
content = content.replace(widget_classes_pattern, "'metric-fuel': 'sm:col-span-5 lg:col-span-5 flex h-full',\n  'chart-fuel-efficiency': 'sm:col-span-10 lg:col-span-6 lg:row-span-2 flex h-full min-h-[350px]',")

# 3. Add to widgetOrder state
widget_order_pattern = r"'chart-revenue', 'chart-weekly-earnings', 'chart-dispatches', 'chart-fleet', 'metric-revenue', 'metric-fuel'"
content = content.replace(widget_order_pattern, "'chart-revenue', 'chart-weekly-earnings', 'chart-dispatches', 'chart-fleet', 'metric-revenue', 'metric-fuel', 'chart-fuel-efficiency'")

# 4. Add Mock Data
mock_data = """
  const fuelEfficiencyData = [
    { time: '05:00', fillUps: 2, avgVolume: 15 },
    { time: '08:00', fillUps: 8, avgVolume: 45 },
    { time: '11:00', fillUps: 12, avgVolume: 60 },
    { time: '14:00', fillUps: 15, avgVolume: 80 },
    { time: '17:00', fillUps: 20, avgVolume: 110 },
    { time: '20:00', fillUps: 5, avgVolume: 25 },
    { time: '23:00', fillUps: 1, avgVolume: 10 },
  ];
"""
fleet_data_pattern = r"const monthlyEarningsData = \[.*?\];"
fleet_match = re.search(fleet_data_pattern, content, flags=re.DOTALL)
if fleet_match:
    content = content.replace(fleet_match.group(0), fleet_match.group(0) + mock_data)

# 5. Add Widget Content
widget_content = """
    'chart-fuel-efficiency': (
        <div className="dark:bg-slate-800 bg-white border dark:border-slate-700 border-slate-200 rounded-3xl p-6 shadow-sm flex flex-col w-full h-full cursor-grab active:cursor-grabbing pointer-events-auto">
          <div className="flex justify-between items-center mb-6">
            <div className="flex items-center gap-3">
              <div className="p-2 bg-emerald-100 dark:bg-emerald-900/30 text-emerald-600 dark:text-emerald-400 rounded-xl">
                <Fuel className="w-5 h-5" />
              </div>
              <div>
                <h2 className="text-lg sm:text-xl font-bold dark:text-white text-slate-900">Fuel Fill-up Frequency & Volume</h2>
                <p className="text-xs text-slate-500 font-medium">When and how much units refuel</p>
              </div>
            </div>
          </div>
          <div className="flex-1 w-full relative min-h-[250px]">
            <ResponsiveContainer width="100%" height="100%">
              <ComposedChart data={fuelEfficiencyData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                <defs>
                  <linearGradient id="fillVolume" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#10b981" stopOpacity={0.3}/>
                    <stop offset="95%" stopColor="#10b981" stopOpacity={0}/>
                  </linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#e2e8f0" opacity={0.5} />
                <XAxis 
                  dataKey="time" 
                  axisLine={false} 
                  tickLine={false} 
                  tick={{ fontSize: 12, fill: '#64748b' }} 
                  dy={10}
                />
                <YAxis 
                  yAxisId="left"
                  axisLine={false} 
                  tickLine={false} 
                  tick={{ fontSize: 12, fill: '#64748b' }}
                />
                <YAxis 
                  yAxisId="right"
                  orientation="right"
                  axisLine={false} 
                  tickLine={false} 
                  tick={{ fontSize: 12, fill: '#64748b' }}
                />
                <Tooltip
                  contentStyle={{ backgroundColor: '#1e293b', borderRadius: '12px', border: 'none', color: '#fff' }}
                  itemStyle={{ color: '#e2e8f0' }}
                  cursor={{ fill: 'transparent' }}
                />
                <Legend iconType="circle" wrapperStyle={{ fontSize: '12px', paddingTop: '10px' }} />
                <Bar yAxisId="left" dataKey="fillUps" name="Fill-up Count" fill="#3b82f6" radius={[4, 4, 0, 0]} barSize={30} />
                <Area yAxisId="right" type="monotone" dataKey="avgVolume" name="Avg Volume (L)" stroke="#10b981" strokeWidth={3} fill="url(#fillVolume)" />
              </ComposedChart>
            </ResponsiveContainer>
          </div>
        </div>
    ),
"""
widget_contents_pattern = r"const widgetContents = \{"
content = content.replace(widget_contents_pattern, "const widgetContents = {" + widget_content)

with open("frontend/src/pages/SuperAdminDashboard.jsx", "w") as f:
    f.write(content)

print("Fuel efficiency board added.")
