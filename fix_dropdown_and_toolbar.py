import re

with open('frontend/src/pages/admin/DriverManagementPage.jsx', 'r') as f:
    content = f.read()

# 1. Remove Filters button and the search wrapper flex div that contains it
filter_button_search = r"<button \s*onClick=\{\(\) => setShowFilters\(!showFilters\)\}\s*className=\"flex items-center gap-2 px-3 py-1\.5 border border-slate-300 rounded-lg text-sm font-medium text-slate-700 hover:bg-slate-50 transition-colors bg-white\"\s*>\s*<Filter className=\"w-4 h-4\" />\s*<span className=\"hidden sm:inline\">Filters</span>\s*</button>"
content = re.sub(filter_button_search, "", content)

# 2. Remove Eye and Grid buttons (and the divider)
toolbar_right_search = r"<div className=\"h-6 w-px bg-slate-200 hidden sm:block\"></div>\s*<div className=\"flex items-center gap-1 shrink-0\">\s*<button className=\"p-1\.5 text-slate-400 hover:text-slate-600 rounded transition-colors\" title=\"Columns\">\s*<Eye className=\"w-4 h-4\" />\s*</button>\s*<button \s*onClick=\{\(\) => setDensity\(d => d === 'comfortable' \? 'compact' : 'comfortable'\)\}\s*className=\"p-1\.5 text-slate-400 hover:text-slate-600 rounded transition-colors\" title=\"Density\"\s*>\s*<LayoutGrid className=\"w-4 h-4\" />\s*</button>\s*</div>"
content = re.sub(toolbar_right_search, "", content)

# 3. Fix Dropdown actions: Archive and Delete
archive_search = r"<button onClick=\{\(\) => setActiveDropdown\(null\)\} className=\"w-full text-left px-4 py-2 text-sm text-slate-700 hover:bg-slate-50\">Archive</button>"
archive_replace = r"""<button onClick={() => {
                            setActiveDropdown(null);
                            setDriversList(prev => prev.map(d => d.id === driver.id ? { ...d, status: 'Inactive' } : d));
                          }} className="w-full text-left px-4 py-2 text-sm text-slate-700 hover:bg-slate-50">Archive</button>"""
content = re.sub(archive_search, archive_replace, content)

delete_search = r"<button onClick=\{\(\) => setActiveDropdown\(null\)\} className=\"w-full text-left px-4 py-2 text-sm text-red-600 hover:bg-red-50 font-medium\">Delete</button>"
delete_replace = r"""<button onClick={() => {
                            setActiveDropdown(null);
                            setDriversList(prev => prev.filter(d => d.id !== driver.id));
                          }} className="w-full text-left px-4 py-2 text-sm text-red-600 hover:bg-red-50 font-medium">Delete</button>"""
content = re.sub(delete_search, delete_replace, content)

# 4. Remove showFilters state
show_filters_search = r"const \[showFilters, setShowFilters\] = useState\(false\);\n"
content = re.sub(show_filters_search, "", content)

# 5. Remove density state
density_search = r"const \[density, setDensity\] = useState\('comfortable'\); // comfortable, compact\n"
content = re.sub(density_search, "", content)

# 6. Remove density from td classes
# Find: className={`px-4 ${density === 'compact' ? 'py-2' : 'py-3'}`}
td_density_search = r"className=\{`px-4 \$\{density === 'compact' \? 'py-2' : 'py-3'\}`\}"
td_density_replace = r'className="px-4 py-3"'
content = re.sub(td_density_search, td_density_replace, content)

with open('frontend/src/pages/admin/DriverManagementPage.jsx', 'w') as f:
    f.write(content)
