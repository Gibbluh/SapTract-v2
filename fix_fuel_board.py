import re

with open("frontend/src/pages/SuperAdminDashboard.jsx", "r") as f:
    content = f.read()

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
          <div className="flex-1 w-full relative min-h-[250px]" onPointerDown={(e) => e.stopPropagation()}>
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

content = content.replace("const widgetContents = {", "const widgetContents = {" + widget_content)

with open("frontend/src/pages/SuperAdminDashboard.jsx", "w") as f:
    f.write(content)

print("Fixed")
