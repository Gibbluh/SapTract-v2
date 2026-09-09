import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# Make the Weekly Earnings chart narrower (lg:col-span-4)
content = content.replace(
    "'chart-weekly-earnings': 'col-span-12 flex h-full min-h-[350px]',",
    "'chart-weekly-earnings': 'col-span-12 lg:col-span-4 flex h-full min-h-[350px]',"
)

# And make chart-dispatches smaller or move it? 
# If chart-revenue is 8, chart-weekly-earnings is 4 -> that's 1 row.
# If chart-dispatches is 4, metric-revenue 4, metric-fuel 4 -> that's 1 row.
# Let's adjust widgetOrder:
# ['chart-revenue', 'chart-weekly-earnings', 'chart-dispatches', 'metric-revenue', 'metric-fuel', 'chart-fleet']
content = content.replace(
    "'chart-revenue', 'chart-dispatches', 'chart-fleet', 'metric-revenue', 'metric-fuel', 'chart-weekly-earnings'",
    "'chart-revenue', 'chart-weekly-earnings', 'chart-dispatches', 'metric-revenue', 'metric-fuel', 'chart-fleet'"
)

# Also need to import Cell
if "Cell," not in content:
    content = content.replace("  Bar,", "  Bar,\n  Cell,")

chart_weekly_jsx = """    'chart-weekly-earnings': (
        <div className="dark:bg-[#1e293b] bg-slate-900 border dark:border-slate-700 border-slate-800 rounded-3xl p-6 shadow-sm flex flex-col w-full h-full cursor-grab active:cursor-grabbing pointer-events-auto">
          <div className="flex flex-col items-start mb-6">
            <span className="text-sm font-medium text-slate-400 mb-1">Daily Sales</span>
            <h2 className="text-3xl font-bold text-white flex items-center gap-2">
              <TrendingUp className="w-5 h-5 text-blue-500" />
              1,340k ₱
            </h2>
          </div>
          <div className="relative flex-1 w-full relative z-10" onPointerDown={(e) => e.stopPropagation()}>
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={weeklyEarningsData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }} barSize={24}>
                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#334155" />
                <XAxis dataKey="day" axisLine={false} tickLine={false} tick={{ fontSize: 12, fill: '#94a3b8' }} dy={10} />
                <YAxis axisLine={false} tickLine={false} tick={{ fontSize: 12, fill: '#94a3b8' }} tickFormatter={(value) => `${value/1000}`} />
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
    ),"""

# Find the old chart-weekly-earnings and replace it
# We know it starts with `'chart-weekly-earnings': (` and ends with `),`
# Let's use a regex to replace the block safely
pattern = r"\s*'chart-weekly-earnings': \(\s*<div.*?(?=\s*'metric-revenue':|\s*\}\s*;)s*'metric-revenue':"
# Actually, since I just wrote it in the previous step, I can do a direct string replace of the previous JSX block.
