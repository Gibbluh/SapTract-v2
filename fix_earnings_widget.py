import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# 1. Add earningsTab state
content = content.replace(
    "const [revenueTab, setRevenueTab] = useState('1d');",
    "const [revenueTab, setRevenueTab] = useState('1d');\n  const [earningsTab, setEarningsTab] = useState('Week');"
)

# 2. Add new mock data
old_mock_data = r"""  const weeklyEarningsData = \[
    \{ day: 'Mon', earnings: 145000 \},
    \{ day: 'Tue', earnings: 132000 \},
    \{ day: 'Wed', earnings: 164000 \},
    \{ day: 'Thu', earnings: 158000 \},
    \{ day: 'Fri', earnings: 195000 \},
    \{ day: 'Sat', earnings: 210000 \},
    \{ day: 'Sun', earnings: 185000 \},
  \];"""

new_mock_data = """  const weeklyEarningsData = [
    { label: 'Mon', earnings: 145000 },
    { label: 'Tue', earnings: 132000 },
    { label: 'Wed', earnings: 164000 },
    { label: 'Thu', earnings: 158000 },
    { label: 'Fri', earnings: 195000 },
    { label: 'Sat', earnings: 210000 },
    { label: 'Sun', earnings: 185000 },
  ];

  const monthlyEarningsData = [
    { label: 'Week 1', earnings: 1105000 },
    { label: 'Week 2', earnings: 1050000 },
    { label: 'Week 3', earnings: 1250000 },
    { label: 'Week 4', earnings: 1189000 },
  ];

  const yearlyEarningsData = [
    { label: 'Jan', earnings: 4500000 },
    { label: 'Feb', earnings: 4200000 },
    { label: 'Mar', earnings: 4800000 },
    { label: 'Apr', earnings: 5100000 },
    { label: 'May', earnings: 4900000 },
    { label: 'Jun', earnings: 5300000 },
    { label: 'Jul', earnings: 5600000 },
    { label: 'Aug', earnings: 5400000 },
    { label: 'Sep', earnings: 5800000 },
    { label: 'Oct', earnings: 5200000 },
    { label: 'Nov', earnings: 5900000 },
    { label: 'Dec', earnings: 6200000 },
  ];"""

content = re.sub(old_mock_data, new_mock_data, content)

# 3. Inject computed properties right before widgetContents
computed_props = """  const currentEarningsData = earningsTab === 'Week' ? weeklyEarningsData : earningsTab === 'Month' ? monthlyEarningsData : yearlyEarningsData;
  const currentEarningsTotal = earningsTab === 'Week' ? '₱1,189,000' : earningsTab === 'Month' ? '₱4,594,000' : '₱62,900,000';
  const earningsColors = ['#3b82f6', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6', '#0ea5e9', '#ec4899', '#14b8a6', '#f43f5e', '#84cc16', '#a855f7', '#06b6d4'];

  const CustomEarningsTooltip = ({ active, payload, label }) => {
    if (active && payload && payload.length) {
      return (
        <div className="dark:bg-slate-800 bg-white border dark:border-slate-700 border-slate-200 p-3 rounded-xl shadow-lg">
          <p className="dark:text-slate-400 text-slate-500 text-xs font-semibold mb-1">{label}</p>
          <p className="dark:text-white text-slate-900 font-bold text-lg">
            ₱{payload[0].value.toLocaleString()}
          </p>
        </div>
      );
    }
    return null;
  };

  const widgetContents = {"""

content = content.replace("  const widgetContents = {", computed_props)

# 4. Replace chart-weekly-earnings JSX
pattern = r"'chart-weekly-earnings': \([\s\S]*?\),\s*'metric-revenue':"

chart_weekly_jsx = """'chart-weekly-earnings': (
        <div className="dark:bg-slate-800 bg-white border dark:border-slate-700 border-slate-200 rounded-3xl p-6 shadow-sm flex flex-col w-full h-full cursor-grab active:cursor-grabbing pointer-events-auto">
          <div className="flex justify-between items-center mb-1">
            <div className="flex items-center gap-3">
              <h2 className="text-lg sm:text-xl font-bold dark:text-white text-slate-900">Earnings Comparison</h2>
            </div>
            <div className="flex dark:bg-slate-900 bg-slate-50 rounded-lg p-1 border dark:border-slate-700 border-slate-200 shadow-sm" onPointerDown={(e) => e.stopPropagation()}>
              {['Week', 'Month', 'Year'].map(tab => (
                <button 
                  key={tab}
                  onClick={() => setEarningsTab(tab)}
                  className={`px-3 py-1 text-xs font-bold rounded shadow-sm border transition-colors ${earningsTab === tab ? 'dark:bg-slate-800 bg-white dark:text-blue-400 text-blue-600 dark:border-slate-600 border-slate-200' : 'border-transparent dark:text-slate-400 text-slate-500 hover:text-slate-700'}`}
                >
                  {tab}
                </button>
              ))}
            </div>
          </div>
          
          <div className="flex items-end gap-3 mb-6">
            <h3 className="text-4xl font-black dark:text-white text-slate-900">{currentEarningsTotal}</h3>
          </div>

          <div className="relative flex-1 w-full min-h-[200px] relative z-10" onPointerDown={(e) => e.stopPropagation()}>
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={currentEarningsData} margin={{ top: 10, right: 10, left: -10, bottom: 0 }} barSize={24}>
                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="currentColor" className="text-slate-200 dark:text-slate-700" />
                <XAxis dataKey="label" axisLine={false} tickLine={false} tick={{ fontSize: 12, fill: 'currentColor' }} className="text-slate-500 dark:text-slate-400" dy={10} />
                <YAxis axisLine={false} tickLine={false} tick={{ fontSize: 12, fill: 'currentColor' }} className="text-slate-500 dark:text-slate-400" tickFormatter={(value) => `${value/1000}k`} />
                <Tooltip cursor={{ fill: 'rgba(148, 163, 184, 0.1)' }} content={<CustomEarningsTooltip />} />
                <Bar dataKey="earnings" radius={[4, 4, 0, 0]}>
                  {currentEarningsData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={earningsColors[index % earningsColors.length]} />
                  ))}
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

