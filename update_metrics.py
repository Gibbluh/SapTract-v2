import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# Replace metric-active, metric-pending, metric-alerts with metric-fuel
# We'll use regex to remove them, then insert metric-fuel

metric_active_regex = r"    'metric-active': \(.*?\n        </div>\n\s+\),\n"
content = re.sub(metric_active_regex, "", content, flags=re.DOTALL)

metric_pending_regex = r"    'metric-pending': \(.*?\n        </div>\n\s+\),\n"
content = re.sub(metric_pending_regex, "", content, flags=re.DOTALL)

metric_alerts_regex = r"    'metric-alerts': \(.*?\n        </div>\n\s+\),\n"
content = re.sub(metric_alerts_regex, "", content, flags=re.DOTALL)

metric_fuel = """    'metric-fuel': (
        <div className="dark:bg-slate-800 bg-white border dark:border-slate-700 border-slate-200 rounded-2xl p-5 shadow-sm relative overflow-hidden flex flex-col w-full h-full cursor-grab active:cursor-grabbing">
          <div className="flex justify-between items-start mb-2">
            <div className="w-10 h-10 dark:bg-amber-900/50 bg-amber-50 rounded-lg flex items-center justify-center">
              <Fuel className="dark:text-amber-400 text-amber-600 w-5 h-5" />
            </div>
            <div className="dark:bg-red-900/50 bg-red-100 dark:text-red-400 text-red-700 text-[10px] font-bold px-2 py-1 rounded-full flex items-center">
              <ArrowUpRight className="w-3 h-3 mr-1" />
              -2.1%
            </div>
          </div>
          <div className="mt-2">
            <p className="text-xs font-medium dark:text-slate-400 text-slate-500 mb-1">Fuel Expense {timeFilter}</p>
            <h2 className="text-2xl sm:text-3xl font-black dark:text-white text-slate-900 tracking-tight">
              {formatCurrency ? formatCurrency(82350 * tfMult) : `₱${(82350 * tfMult).toLocaleString()}`}
            </h2>
          </div>
          <div className="mt-auto pt-4 flex justify-between items-end">
            <p className="text-[11px] dark:text-slate-500 text-slate-400">vs ₱{(84120 * tfMult).toLocaleString()} previous</p>
            <div className="flex items-end gap-1">
              <div className="w-2 dark:bg-amber-400 bg-amber-600 rounded-sm h-4"></div>
              <div className="w-2 dark:bg-amber-400 bg-amber-600 rounded-sm h-6"></div>
              <div className="w-2 dark:bg-amber-400 bg-amber-600 rounded-sm h-3"></div>
              <div className="w-2 dark:bg-slate-700 bg-slate-200 rounded-sm h-7"></div>
            </div>
          </div>
        </div>
    ),
"""

# Insert metric-fuel after metric-revenue
content = content.replace("    'metric-users': (", metric_fuel + "    'metric-users': (")

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
