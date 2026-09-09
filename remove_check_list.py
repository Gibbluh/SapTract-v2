import re

with open('frontend/src/pages/admin/DriverManagementPage.jsx', 'r') as f:
    content = f.read()

# 1. Remove Bulk Action Bar
bulk_search = r"\{\s*selectedDrivers\.size > 0 && \(\s*<div className=\"absolute top-6 left-1/2 -translate-x-1/2 z-30 bg-blue-600 text-white px-4 py-3 rounded-lg shadow-xl flex items-center gap-4 animate-in slide-in-from-top-4\">\s*<span className=\"font-semibold text-sm\">\{selectedDrivers\.size\} drivers selected</span>\s*<div className=\"h-4 w-px bg-blue-400\"></div>\s*<button className=\"text-sm font-medium hover:text-blue-100 transition-colors\">Change Status</button>\s*<button className=\"text-sm font-medium hover:text-blue-100 transition-colors\">Download QRs</button>\s*<button className=\"text-sm font-medium hover:text-blue-100 transition-colors\">Export \(CSV\)</button>\s*<button className=\"text-sm font-medium hover:text-red-300 transition-colors\">Archive</button>\s*<div className=\"h-4 w-px bg-blue-400\"></div>\s*<button onClick=\{\(\) => setSelectedDrivers\(new Set\(\)\)\} className=\"p-1 hover:bg-blue-700 rounded transition-colors\">\s*<X className=\"w-4 h-4\" />\s*</button>\s*</div>\s*\)\}"
content = re.sub(bulk_search, "", content)

# 2. Remove table header checkbox
th_search = r"<th className=\"px-4 py-3 w-10\">\s*<input \s*type=\"checkbox\" \s*className=\"rounded border-slate-300 text-blue-600 focus:ring-blue-500\"\s*checked=\{selectedDrivers\.size === paginatedDrivers\.length && paginatedDrivers\.length > 0\}\s*onChange=\{toggleAll\}\s*/>\s*</th>"
content = re.sub(th_search, "", content)

# 3. Remove table body checkbox
td_search = r"<td className=\{`px-4 \$\{density === 'compact' \? 'py-2' : 'py-3'\}`\}>\s*<input \s*type=\"checkbox\" \s*className=\"rounded border-slate-300 text-blue-600 focus:ring-blue-500\"\s*checked=\{selectedDrivers\.has\(driver\.id\)\}\s*onChange=\{\(\) => toggleSelection\(driver\.id\)\}\s*onClick=\{e => e\.stopPropagation\(\)\}\s*/>\s*</td>"
content = re.sub(td_search, "", content)

# 4. Modify onClick condition
onclick_search = r"if \(e\.target\.type !== 'checkbox' && !e\.target\.closest\('button'\)\) \{"
onclick_replace = r"if (!e.target.closest('button')) {"
content = content.replace(onclick_search, onclick_replace)

# 5. Modify colSpan
colspan_search = r"<td colSpan=\{9\} className=\"py-12 text-center text-slate-500\">"
colspan_replace = r'<td colSpan={6} className="py-12 text-center text-slate-500">'
content = content.replace(colspan_search, colspan_replace)

# 6. Remove states and handlers
state_search = r"const \[selectedDrivers, setSelectedDrivers\] = useState\(new Set\(\)\);\n"
content = content.replace(state_search, "")

toggle_selection_search = r"const toggleSelection = \(id\) => \{\s*const newSet = new Set\(selectedDrivers\);\s*if \(newSet\.has\(id\)\) newSet\.delete\(id\);\s*else newSet\.add\(id\);\s*setSelectedDrivers\(newSet\);\s*\};\s*const toggleAll = \(\) => \{\s*if \(selectedDrivers\.size === paginatedDrivers\.length\) \{\s*setSelectedDrivers\(newSet\(\)\);\s*\} else \{\s*setSelectedDrivers\(new Set\(paginatedDrivers\.map\(d => d\.id\)\)\);\s*\}\s*\};\s*"
# Since `newSet()` was a typo in the original (should be `new Set()`), I'll just use regex.
toggle_regex = r"const toggleSelection = \(id\) => \{[\s\S]*?const toggleAll = \(\) => \{[\s\S]*?\};\s*"
content = re.sub(toggle_regex, "", content)

with open('frontend/src/pages/admin/DriverManagementPage.jsx', 'w') as f:
    f.write(content)
