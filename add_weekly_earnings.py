import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# 1. Update imports
content = content.replace(
    "  AreaChart,\n  Area,\n  XAxis,",
    "  AreaChart,\n  Area,\n  BarChart,\n  Bar,\n  XAxis,"
)

# 2. Add WIDGET_CLASSES entry
content = content.replace(
    "'chart-fleet': 'col-span-12 lg:col-span-4 flex h-full',",
    "'chart-fleet': 'col-span-12 lg:col-span-4 flex h-full',\n  'chart-weekly-earnings': 'col-span-12 flex h-full',"
)

# 3. Add to widgetOrder
content = content.replace(
    "'chart-revenue', 'chart-dispatches', 'chart-fleet', 'metric-revenue', 'metric-fuel'",
    "'chart-revenue', 'chart-dispatches', 'chart-fleet', 'metric-revenue', 'metric-fuel', 'chart-weekly-earnings'"
)

# 4. Add mock data
mock_data = """  const mockRevenueData = ["""
new_mock_data = """  const weeklyEarningsData = [
    { day: 'Mon', earnings: 145000 },
    { day: 'Tue', earnings: 132000 },
    { day: 'Wed', earnings: 164000 },
    { day: 'Thu', earnings: 158000 },
    { day: 'Fri', earnings: 195000 },
    { day: 'Sat', earnings: 210000 },
    { day: 'Sun', earnings: 185000 },
  ];

  const mockRevenueData = ["""
content = content.replace(mock_data, new_mock_data)

# 5. Add widget to widgetContents
# find end of widgetContents (before `  const sensors = useSensors(` but actually wait, widgetContents is declared inside the component, let's inject at the end of the `widgetContents` object).
# Looking at the file, widgetContents ends with `'chart-dispatches': ( ... ) }` or similar. Let's find `'chart-dispatches'` and the end of it.
# Wait, I know `widgetContents` ends with:
#               </div>
#             ))}
#           </div>
#         </div>
#     )
#   };
# 
# Actually, let's just use regex to insert before `  };` or I can find `'chart-dispatches': (` and go to its end.

chart_weekly_jsx = """    'chart-weekly-earnings': (
        <div className="dark:bg-slate-800 bg-white border dark:border-slate-700 border-slate-200 rounded-3xl p-6 shadow-sm flex flex-col w-full h-full cursor-grab active:cursor-grabbing pointer-events-auto">
          <div className="flex justify-between items-center mb-6">
            <h2 className="text-lg font-bold dark:text-white text-slate-900 flex items-center gap-2">
              <TrendingUp className="w-5 h-5 dark:text-blue-400 text-blue-500" />
              Weekly Earnings Comparison
            </h2>
          </div>
          <div className="relative h-64 w-full relative z-10" onPointerDown={(e) => e.stopPropagation()}>
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={weeklyEarningsData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }} barSize={32}>
                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="currentColor" className="text-slate-200 dark:text-slate-700" />
                <XAxis dataKey="day" axisLine={false} tickLine={false} tick={{ fontSize: 12, fill: 'currentColor' }} className="text-slate-500" dy={10} />
                <YAxis axisLine={false} tickLine={false} tick={{ fontSize: 12, fill: 'currentColor' }} className="text-slate-500" tickFormatter={(value) => `₱${value/1000}k`} />
                <Tooltip 
                  cursor={{ fill: 'var(--tw-colors-slate-100)' }} 
                  contentStyle={{ borderRadius: '12px', border: 'none', boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)', backgroundColor: 'var(--tw-colors-slate-800)', color: 'white' }}
                  formatter={(value) => [`₱${value.toLocaleString()}`, 'Earnings']}
                />
                <Bar dataKey="earnings" fill="#3b82f6" radius={[6, 6, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
    ),
"""
# Need to insert this inside `widgetContents`.
# I'll just look for `  const sensors = useSensors` which is defined right after `widgetOrder` and before `handleDragStart`. Wait, `widgetContents` is defined after `const mockRevenueData`!
# Let's check where `widgetContents` is defined.
