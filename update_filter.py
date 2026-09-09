with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

old_filter_html = """        <div className="flex justify-between items-center bg-white dark:bg-slate-800 p-4 rounded-2xl border border-slate-200 dark:border-slate-700 shadow-sm">
          <h2 className="text-lg font-bold text-slate-900 dark:text-white">Dashboard Overview</h2>
          <div className="flex dark:bg-slate-900 bg-slate-50 rounded-lg p-1 border dark:border-slate-700 border-slate-200">
            <button 
              onClick={() => setTimeFilter('Today')}
              className={`px-4 py-1.5 text-xs font-bold rounded shadow-sm border transition-colors ${timeFilter === 'Today' ? 'dark:bg-slate-800 bg-white dark:text-blue-400 text-blue-600 dark:border-slate-600 border-slate-200' : 'border-transparent dark:text-slate-400 text-slate-500 hover:text-slate-700'}`}
            >Today</button>
            <button 
              onClick={() => setTimeFilter('7 Days')}
              className={`px-4 py-1.5 text-xs font-bold rounded shadow-sm border transition-colors ${timeFilter === '7 Days' ? 'dark:bg-slate-800 bg-white dark:text-blue-400 text-blue-600 dark:border-slate-600 border-slate-200' : 'border-transparent dark:text-slate-400 text-slate-500 hover:text-slate-700'}`}
            >7 Days</button>
            <button 
              onClick={() => setTimeFilter('30 Days')}
              className={`px-4 py-1.5 text-xs font-bold rounded shadow-sm border transition-colors ${timeFilter === '30 Days' ? 'dark:bg-slate-800 bg-white dark:text-blue-400 text-blue-600 dark:border-slate-600 border-slate-200' : 'border-transparent dark:text-slate-400 text-slate-500 hover:text-slate-700'}`}
            >30 Days</button>
          </div>
        </div>"""

new_filter_html = """        <div className="flex justify-between items-end mb-2 px-1">
          <h2 className="text-2xl font-black text-slate-900 dark:text-white tracking-tight">Dashboard Overview</h2>
          <div className="flex dark:bg-slate-900 bg-slate-50 rounded-lg p-1 border dark:border-slate-700 border-slate-200 shadow-sm">
            <button 
              onClick={() => setTimeFilter('Yesterday')}
              className={`px-4 py-1.5 text-xs font-bold rounded shadow-sm border transition-colors ${timeFilter === 'Yesterday' ? 'dark:bg-slate-800 bg-white dark:text-blue-400 text-blue-600 dark:border-slate-600 border-slate-200' : 'border-transparent dark:text-slate-400 text-slate-500 hover:text-slate-700'}`}
            >Yesterday</button>
            <button 
              onClick={() => setTimeFilter('Today')}
              className={`px-4 py-1.5 text-xs font-bold rounded shadow-sm border transition-colors ${timeFilter === 'Today' ? 'dark:bg-slate-800 bg-white dark:text-blue-400 text-blue-600 dark:border-slate-600 border-slate-200' : 'border-transparent dark:text-slate-400 text-slate-500 hover:text-slate-700'}`}
            >Today</button>
            <button 
              onClick={() => setTimeFilter('Tomorrow')}
              className={`px-4 py-1.5 text-xs font-bold rounded shadow-sm border transition-colors ${timeFilter === 'Tomorrow' ? 'dark:bg-slate-800 bg-white dark:text-blue-400 text-blue-600 dark:border-slate-600 border-slate-200' : 'border-transparent dark:text-slate-400 text-slate-500 hover:text-slate-700'}`}
            >Tomorrow</button>
          </div>
        </div>"""

content = content.replace(old_filter_html, new_filter_html)

old_tfmult = "const tfMult = timeFilter === '30 Days' ? 30 : timeFilter === '7 Days' ? 7 : 1;"
new_tfmult = "const tfMult = timeFilter === 'Tomorrow' ? 1.25 : timeFilter === 'Yesterday' ? 0.8 : 1;"
content = content.replace(old_tfmult, new_tfmult)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
