import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# I will rewrite the entire chart-dispatches block
dispatches_regex = r"    'chart-dispatches': \(.*?\n        </div>\n      \n    \)\n  \};\n\n  return \("
# Let's verify we catch it properly

new_dispatches = """    'chart-dispatches': (
        <div className="dark:bg-slate-800 bg-white border dark:border-slate-700 border-slate-200 rounded-3xl p-6 shadow-sm flex flex-col w-full h-full cursor-grab active:cursor-grabbing pointer-events-auto">
          <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-4 gap-3">
            <h2 className="text-lg font-bold dark:text-white text-slate-900 flex items-center gap-2">
              <Activity className="w-5 h-5 dark:text-blue-400 text-blue-500" />
              Today's Dispatches
            </h2>
            
            {/* Time Tabs */}
            <div className="flex bg-slate-100 dark:bg-slate-900/50 p-1 rounded-lg border border-slate-200 dark:border-slate-700 pointer-events-auto" onPointerDown={(e) => e.stopPropagation()}>
              {['Yesterday', 'Today', 'Tomorrow'].map(tab => (
                <button
                  key={tab}
                  onClick={() => setTimeFilter(tab)}
                  className={`px-3 py-1 text-xs font-bold rounded-md transition-colors ${timeFilter === tab ? 'bg-white dark:bg-slate-700 text-blue-600 dark:text-blue-400 shadow-sm' : 'text-slate-500 hover:text-slate-700 dark:hover:text-slate-300'}`}
                >
                  {tab}
                </button>
              ))}
            </div>
          </div>

          {/* Active Drivers Status Header */}
          <div className="flex justify-between items-center bg-blue-50/50 dark:bg-blue-900/20 px-4 py-2 rounded-xl mb-4 border border-blue-100 dark:border-blue-800/50">
             <span className="text-xs font-semibold text-slate-600 dark:text-slate-300">Active Drivers for {timeFilter}</span>
             <span className="text-sm font-bold text-blue-600 dark:text-blue-400 flex items-center"><Users className="w-4 h-4 mr-1.5" /> 14 Online</span>
          </div>
          
          {/* Vertical Leaderboard / Messenger-style List */}
          <div className="flex flex-col gap-3 overflow-y-auto pr-2 relative z-20" style={{ maxHeight: '380px' }} onPointerDown={(e) => e.stopPropagation()}>
            {MOCK_DISPATCHES.map((driver) => (
              <div key={driver.id} className="flex items-center p-3 rounded-2xl border dark:border-slate-700 border-slate-100 dark:bg-slate-900/50 bg-white hover:bg-slate-50 dark:hover:bg-slate-800 hover:border-blue-200 dark:hover:border-blue-500/50 transition-all cursor-pointer shadow-sm group">
                <div className="relative shrink-0 mr-4">
                  <img src={driver.avatar} alt={driver.name} className="w-12 h-12 rounded-full object-cover border-2 dark:border-slate-700 border-slate-200 group-hover:border-blue-400 transition-colors" />
                  <span className="absolute bottom-0 right-0 w-3.5 h-3.5 rounded-full bg-emerald-500 border-2 border-white dark:border-slate-800"></span>
                </div>
                
                <div className="flex-1 min-w-0 flex flex-col justify-center">
                  <h4 className="text-sm font-bold dark:text-white text-slate-900 truncate">{driver.name}</h4>
                  <div className="flex items-center text-[11px] font-medium text-slate-500 dark:text-slate-400 gap-2 mt-0.5">
                    <span className="flex items-center dark:text-blue-400 text-blue-600 truncate"><Truck className="w-3 h-3 mr-1" /> {driver.vehicle}</span>
                    <span className="w-1 h-1 rounded-full bg-slate-300 dark:bg-slate-600 shrink-0"></span>
                    <span className="truncate">{driver.route}</span>
                  </div>
                </div>

                <div className="shrink-0 ml-3">
                   <button className="text-[10px] font-bold dark:bg-slate-800 bg-slate-100 dark:text-slate-300 text-slate-700 px-3 py-1.5 rounded-full group-hover:bg-blue-50 group-hover:text-blue-600 dark:group-hover:bg-blue-900/30 dark:group-hover:text-blue-400 transition-colors">
                     View
                   </button>
                </div>
              </div>
            ))}
          </div>
        </div>
    )
  };

  return ("""

content = re.sub(dispatches_regex, new_dispatches, content, flags=re.DOTALL)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
