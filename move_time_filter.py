import re

with open("frontend/src/pages/RoleDashboard.jsx", "r") as f:
    content = f.read()

# Add timeFilter state
state_code = """
  const [timeFilter, setTimeFilter] = useState('Today');
"""
content = content.replace("const [loading, setLoading] = useState(true);", "const [loading, setLoading] = useState(true);\n" + state_code)

# Add Time Filter to header
header_pattern = r'\{/\* Page Header \*/\}.*?<h1 className="text-2xl font-bold text-slate-900 tracking-tight">Dashboard Overview</h1>\s*</div>'
header_match = re.search(header_pattern, content, flags=re.DOTALL)
if header_match:
    old_header = header_match.group(0)
    new_header = old_header + """
          <div className="flex dark:bg-slate-900 bg-slate-50 rounded-lg p-1 border dark:border-slate-700 border-slate-200 shadow-sm shrink-0">
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
"""
    content = content.replace(old_header, new_header)

# Pass down to SuperAdminDashboard
content = content.replace("<SuperAdminDashboard ", "<SuperAdminDashboard \n            timeFilter={timeFilter}")

with open("frontend/src/pages/RoleDashboard.jsx", "w") as f:
    f.write(content)

# Now modify SuperAdminDashboard.jsx to accept timeFilter as prop and remove its own state
with open("frontend/src/pages/SuperAdminDashboard.jsx", "r") as f:
    content2 = f.read()

content2 = content2.replace("const SuperAdminDashboard = ({ dashboard, fleetHealth, formatCurrency }) => {", "const SuperAdminDashboard = ({ dashboard, fleetHealth, formatCurrency, timeFilter }) => {")
content2 = content2.replace("const [timeFilter, setTimeFilter] = useState('Today');", "")

# Remove the timeFilter rendering from SuperAdminDashboard.jsx
time_filter_pattern = r'<div className="flex justify-end items-end mb-2 px-1">.*?</div>\s*</div>'
time_filter_match = re.search(time_filter_pattern, content2, flags=re.DOTALL)
if time_filter_match:
    content2 = content2.replace(time_filter_match.group(0), "")

with open("frontend/src/pages/SuperAdminDashboard.jsx", "w") as f:
    f.write(content2)

print("Time filter moved.")
