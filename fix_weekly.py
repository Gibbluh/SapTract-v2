import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# Make them both 6 columns to sit side-by-side (50/50)
content = content.replace(
    "'chart-revenue': 'col-span-12 lg:col-span-8 flex h-full',",
    "'chart-revenue': 'col-span-12 lg:col-span-6 flex h-full',"
)

content = content.replace(
    "'chart-weekly-earnings': 'col-span-12 lg:col-span-4 flex h-full min-h-[350px]',",
    "'chart-weekly-earnings': 'col-span-12 lg:col-span-6 flex h-full min-h-[350px]',"
)

# Update chart-weekly-earnings to use the exact same aesthetic classes as chart-revenue
# but keep the bar chart mechanics (with a standard blue color this time).

pattern = r"'chart-weekly-earnings': \([\s\S]*?\),\s*'metric-revenue':"

chart_weekly_jsx = """'chart-weekly-earnings': (
        <div className="dark:bg-slate-800 bg-white border dark:border-slate-700 border-slate-200 rounded-3xl p-6 shadow-sm flex flex-col w-full h-full cursor-grab active:cursor-grabbing pointer-events-auto">
          <div className="flex justify-between items-center mb-1">
            <div className="flex items-center gap-3">
              <h2 className="text-lg sm:text-xl font-bold dark:text-white text-slate-900">Weekly Earnings</h2>
              <span className="dark:bg-blue-900/50 bg-blue-50 dark:text-blue-400 text-blue-600 text-xs font-semibold px-2.5 py-0.5 rounded-full border dark:border-blue-800 border-blue-100">This Week</span>
            </div>
          </div>
          
          <div className="flex items-end gap-3 mb-6">
            <h3 className="text-4xl font-black dark:text-white text-slate-900">₱1,189,000</h3>
          </div>

          <div className="relative flex-1 w-full min-h-[200px] relative z-10" onPointerDown={(e) => e.stopPropagation()}>
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={weeklyEarningsData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }} barSize={24}>
                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="currentColor" className="text-slate-200 dark:text-slate-700" />
                <XAxis dataKey="day" axisLine={false} tickLine={false} tick={{ fontSize: 12, fill: 'currentColor' }} className="text-slate-500 dark:text-slate-400" dy={10} />
                <YAxis axisLine={false} tickLine={false} tick={{ fontSize: 12, fill: 'currentColor' }} className="text-slate-500 dark:text-slate-400" tickFormatter={(value) => `${value/1000}k`} />
                <Tooltip 
                  cursor={{ fill: 'var(--tw-colors-slate-100)', opacity: 0.1 }} 
                  contentStyle={{ borderRadius: '12px', border: 'none', boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)', backgroundColor: 'var(--tw-colors-slate-800)', color: 'white' }}
                  formatter={(value) => [`₱${value.toLocaleString()}`, 'Earnings']}
                  itemStyle={{ color: '#60a5fa' }}
                />
                <Bar dataKey="earnings" fill="#3b82f6" radius={[4, 4, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
    ),
    'metric-revenue':"""

content = re.sub(pattern, chart_weekly_jsx, content)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)

