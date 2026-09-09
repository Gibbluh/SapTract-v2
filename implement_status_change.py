import re

with open('frontend/src/pages/admin/DriverManagementPage.jsx', 'r') as f:
    content = f.read()

# 1. Add driversList state
state_search = r"const \[rowsPerPage, setRowsPerPage\] = useState\(10\);"
state_replace = r"const [rowsPerPage, setRowsPerPage] = useState(10);\n  const [driversList, setDriversList] = useState(MOCK_DRIVERS);"
content = re.sub(state_search, state_replace, content)

# 2. Update filteredDrivers to use driversList
filtered_search = r"const filteredDrivers = useMemo\(\(\) => \{\s*return MOCK_DRIVERS\.filter\(d => \{"
filtered_replace = r"""const filteredDrivers = useMemo(() => {
    return driversList.filter(d => {"""
content = re.sub(filtered_search, filtered_replace, content)

# 3. Replace StatusBadge in Drawer Header with Select
badge_search = r"<StatusBadge status=\{selectedDriverData\.status\} />"
badge_replace = r"""<select 
                        value={selectedDriverData.status}
                        onChange={(e) => {
                          const newStatus = e.target.value;
                          setDriversList(prev => prev.map(d => d.id === selectedDriverData.id ? { ...d, status: newStatus } : d));
                          setSelectedDriverData(prev => ({ ...prev, status: newStatus }));
                        }}
                        className={`text-xs font-bold px-2 py-1 rounded-full border cursor-pointer outline-none appearance-none ${
                          selectedDriverData.status === 'Active' ? 'bg-emerald-50 text-emerald-700 border-emerald-200' : 
                          selectedDriverData.status === 'Suspended' ? 'bg-red-50 text-red-700 border-red-200' :
                          selectedDriverData.status === 'On Leave' ? 'bg-amber-50 text-amber-700 border-amber-200' :
                          'bg-slate-50 text-slate-700 border-slate-200'
                        }`}
                        style={{ paddingRight: '1rem', backgroundPosition: 'right 0.25rem center', backgroundImage: 'url("data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' fill=\'none\' viewBox=\'0 0 20 20\'%3E%3Cpath stroke=\'%236b7280\' stroke-linecap=\'round\' stroke-linejoin=\'round\' stroke-width=\'1.5\' d=\'M6 8l4 4 4-4\'/%3E%3C/svg%3E")', backgroundRepeat: 'no-repeat', backgroundSize: '1.25rem' }}
                      >
                        <option value="Active">Active</option>
                        <option value="On Leave">On Leave</option>
                        <option value="Suspended">Suspended</option>
                        <option value="Inactive">Inactive</option>
                      </select>"""
# Note: we need to ensure we don't accidentally replace ALL StatusBadges, just the one in the drawer header.
# Actually, the string `<StatusBadge status={selectedDriverData.status} />` only appears in the Drawer Header because the table one uses `driver.status`!
content = content.replace("<StatusBadge status={selectedDriverData.status} />", badge_replace)

# Make sure we also update the dot color in the avatar to be reactive, wait it is reactive: 
# selectedDriverData.status === 'Active' ? 'bg-emerald-500' : 'bg-slate-400' 
# Let's fix that dot to be more robust for all statuses!
dot_search = r"\$\{selectedDriverData\.status === 'Active' \? 'bg-emerald-500' : 'bg-slate-400'\}"
dot_replace = r"${selectedDriverData.status === 'Active' ? 'bg-emerald-500' : selectedDriverData.status === 'Suspended' ? 'bg-red-500' : selectedDriverData.status === 'On Leave' ? 'bg-amber-500' : 'bg-slate-400'}"
content = content.replace(dot_search, dot_replace)

# Also let's update the dropdown actions in the table to actually change the state!
# Wait, the prompt says "Also for their status, I need a way to change this as a super admin".
# Doing it in the drawer is exactly what's needed. Let's make sure the table updates properly too. Yes, it will because driversList is updated.

# What about the dropdown in the table: "{driver.status === 'Active' ? 'Suspend' : 'Activate'}"
table_action_search = r"<button onClick=\{\(\) => setActiveDropdown\(null\)\} className=\"w-full text-left px-4 py-2 text-sm text-slate-700 hover:bg-slate-50\">\{driver.status === 'Active' \? 'Suspend' : 'Activate'\}</button>"
table_action_replace = r"""<button onClick={() => {
                            setActiveDropdown(null);
                            const newStatus = driver.status === 'Active' ? 'Suspended' : 'Active';
                            setDriversList(prev => prev.map(d => d.id === driver.id ? { ...d, status: newStatus } : d));
                          }} className="w-full text-left px-4 py-2 text-sm text-slate-700 hover:bg-slate-50">{driver.status === 'Active' ? 'Suspend' : 'Activate'}</button>"""
content = re.sub(table_action_search, table_action_replace, content)

with open('frontend/src/pages/admin/DriverManagementPage.jsx', 'w') as f:
    f.write(content)
