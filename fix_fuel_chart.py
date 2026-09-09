import re

with open("frontend/src/pages/SuperAdminDashboard.jsx", "r") as f:
    content = f.read()

# Replace the complicated composed chart with a much simpler Bar chart setup
old_chart = """              <ComposedChart data={fuelEfficiencyData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
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
              </ComposedChart>"""

new_chart = """              <BarChart data={fuelEfficiencyData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }} barSize={32}>
                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="currentColor" className="text-slate-200 dark:text-slate-700" />
                <XAxis 
                  dataKey="time" 
                  axisLine={false} 
                  tickLine={false} 
                  tick={{ fontSize: 12, fill: 'currentColor' }} 
                  className="text-slate-500 dark:text-slate-400"
                  dy={10}
                />
                <YAxis 
                  axisLine={false} 
                  tickLine={false} 
                  tick={{ fontSize: 12, fill: 'currentColor' }} 
                  className="text-slate-500 dark:text-slate-400"
                />
                <Tooltip
                  cursor={{ fill: 'rgba(148, 163, 184, 0.1)' }}
                  contentStyle={{ backgroundColor: '#1e293b', borderRadius: '12px', border: 'none', color: '#fff' }}
                  itemStyle={{ color: '#e2e8f0' }}
                />
                <Legend iconType="circle" wrapperStyle={{ fontSize: '12px', paddingTop: '10px' }} />
                <Bar dataKey="fillUps" name="Refuel Count" fill="#10b981" radius={[6, 6, 0, 0]} />
              </BarChart>"""

content = content.replace(old_chart, new_chart)

with open("frontend/src/pages/SuperAdminDashboard.jsx", "w") as f:
    f.write(content)

print("Fixed")
