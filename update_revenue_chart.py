import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

old_chart_revenue = r"""    'chart-revenue': \(.*?<div className="flex justify-between items-center mb-1">.*?<div className="flex items-center gap-3">.*?<h2 className="text-lg sm:text-xl font-bold dark:text-white text-slate-900">Revenue Overview</h2>.*?<span className="dark:bg-blue-900/50 bg-blue-50 dark:text-blue-400 text-blue-600 text-xs font-semibold px-2\.5 py-0\.5 rounded-full border dark:border-blue-800 border-blue-100">Live Feed</span>.*?</div>.*?</div>.*?<p className="text-xs dark:text-slate-400 text-slate-500 mb-8">Real-time gross passenger fares & collection analytics</p>"""

new_chart_revenue_top = """    'chart-revenue': (
        <div className="dark:bg-slate-800 bg-white border dark:border-slate-700 border-slate-200 rounded-3xl p-6 shadow-sm flex flex-col w-full h-full cursor-grab active:cursor-grabbing">
          <div className="flex justify-between items-center mb-1">
            <div className="flex items-center gap-3">
              <h2 className="text-lg sm:text-xl font-bold dark:text-white text-slate-900">Revenue Overview</h2>
              <span className="dark:bg-blue-900/50 bg-blue-50 dark:text-blue-400 text-blue-600 text-xs font-semibold px-2.5 py-0.5 rounded-full border dark:border-blue-800 border-blue-100">Live Feed</span>
            </div>
            
            {/* Revenue Internal Tabs */}
            <div className="flex bg-slate-100 dark:bg-slate-900/50 p-1 rounded-lg border border-slate-200 dark:border-slate-700 pointer-events-auto" onPointerDown={(e) => e.stopPropagation()}>
              {['Today', 'Last Week', 'Last Month'].map(tab => (
                <button
                  key={tab}
                  onClick={() => setRevenueTab(tab)}
                  className={`px-3 py-1 text-[10px] font-bold rounded-md transition-colors ${revenueTab === tab ? 'bg-white dark:bg-slate-700 text-blue-600 dark:text-blue-400 shadow-sm' : 'text-slate-500 hover:text-slate-700 dark:hover:text-slate-300'}`}
                >
                  {tab}
                </button>
              ))}
            </div>
          </div>
          <p className="text-xs dark:text-slate-400 text-slate-500 mb-6">Real-time gross passenger fares & collection analytics</p>"""

content = re.sub(old_chart_revenue, new_chart_revenue_top, content, flags=re.DOTALL)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
