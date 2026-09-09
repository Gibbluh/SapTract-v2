import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

pattern = r"'chart-weekly-earnings': \([\s\S]*?\),\s*'metric-revenue':"

chart_weekly_jsx = """'chart-weekly-earnings': (
        <div className="dark:bg-[#1e293b] bg-slate-900 border dark:border-slate-700 border-slate-800 rounded-3xl p-6 shadow-sm flex flex-col w-full h-full cursor-grab active:cursor-grabbing pointer-events-auto">
          <div className="flex flex-col items-start mb-6">
            <span className="text-sm font-medium text-slate-400 mb-1">Daily Sales</span>
            <h2 className="text-3xl font-bold text-white flex items-center gap-2">
              <TrendingUp className="w-5 h-5 text-blue-500" />
              1,189k ₱
            </h2>
          </div>
          <div className="relative flex-1 w-full relative z-10" onPointerDown={(e) => e.stopPropagation()}>
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={weeklyEarningsData} margin={{ top: 10, right: 10, left: -25, bottom: 0 }} barSize={18}>
                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#334155" />
                <XAxis dataKey="day" axisLine={false} tickLine={false} tick={{ fontSize: 11, fill: '#94a3b8' }} dy={10} />
                <YAxis axisLine={false} tickLine={false} tick={{ fontSize: 11, fill: '#94a3b8' }} tickFormatter={(value) => `${value/1000}`} />
                <Tooltip 
                  cursor={{ fill: '#334155', opacity: 0.4 }} 
                  contentStyle={{ borderRadius: '12px', border: '1px solid #475569', backgroundColor: '#0f172a', color: 'white' }}
                  formatter={(value) => [`₱${value.toLocaleString()}`, 'Earnings']}
                  itemStyle={{ color: '#38bdf8' }}
                />
                <Bar dataKey="earnings" radius={[2, 2, 0, 0]}>
                  {weeklyEarningsData.map((entry, index) => {
                    const colors = ['#3b82f6', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6', '#06b6d4', '#ec4899'];
                    return <Cell key={`cell-${index}`} fill={`${colors[index % colors.length]}33`} stroke={colors[index % colors.length]} strokeWidth={2} />;
                  })}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
    ),
    'metric-revenue':"""

content = re.sub(pattern, chart_weekly_jsx, content)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
