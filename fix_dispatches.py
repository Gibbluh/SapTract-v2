import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# 1. Rename Today's Dispatches to Today's Driver
content = content.replace("Today's Dispatches", "Today's Driver")

# 2. Update Active Drivers Header to match the minimalist style
old_active_header = r"""          \{/\* Active Drivers Status Header \*/\}.*?          </div>"""
new_active_header = """          {/* Active Drivers Status Header */}
          <div className="flex justify-between items-center px-4 py-2.5 rounded-2xl mb-4 border border-slate-200 dark:border-slate-700 bg-transparent">
             <span className="text-[11px] font-medium text-slate-500 dark:text-slate-400">Active Drivers for {timeFilter}</span>
             <span className="text-xs font-bold text-blue-600 dark:text-blue-400 flex items-center"><Users className="w-3.5 h-3.5 mr-1" /> 14 Online</span>
          </div>"""
content = re.sub(old_active_header, new_active_header, content, flags=re.DOTALL)

# 3. Remove "View" button from the list items
view_btn_regex = r"""                <div className="shrink-0 ml-3">.*?</div>"""
content = re.sub(view_btn_regex, "", content, flags=re.DOTALL)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
