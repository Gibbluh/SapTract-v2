import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

old_pill = r"""            \{/\* Active Drivers Pill \*/\}
            <div className="flex items-center gap-4 px-4 py-2 rounded-2xl border border-blue-100 dark:border-blue-900/30 bg-blue-50/20 dark:bg-blue-900/10">
               <span className="text-xs font-medium text-slate-600 dark:text-slate-400">Active Drivers for Today</span>
               <div className="flex items-center text-sm font-bold text-blue-600 dark:text-blue-400">
                 <Users className="w-4 h-4 mr-1.5" /> 14 Online
               </div>
            </div>"""

new_pill = """            {/* Active Drivers Count */}
            <div className="flex items-center text-sm font-bold text-blue-600 dark:text-blue-400">
              <Users className="w-4 h-4 mr-1.5" /> 14 Online
            </div>"""

content = re.sub(old_pill, new_pill, content)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
