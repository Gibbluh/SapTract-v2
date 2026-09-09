import re

with open('frontend/src/pages/admin/DriverManagementPage.jsx', 'r') as f:
    content = f.read()

# Make the MoreVertical button show a dropdown
dropdown_search = r'<td className="px-4 text-right">\s*<button className="p-1\.5 text-slate-400 hover:text-slate-700 rounded-md hover:bg-slate-100 transition-colors opacity-0 group-hover:opacity-100 focus:opacity-100">\s*<MoreVertical className="w-4 h-4" />\s*</button>\s*</td>'
dropdown_replace = r"""<td className="px-4 text-right relative">
                      <button 
                        className="p-1.5 text-slate-400 hover:text-slate-700 rounded-md hover:bg-slate-100 transition-colors opacity-0 group-hover:opacity-100 focus:opacity-100"
                        onClick={(e) => {
                          e.stopPropagation();
                          // Just open drawer for View Profile, or theoretically toggle a local state for dropdown
                          openDriverDrawer(driver);
                        }}
                      >
                        <MoreVertical className="w-4 h-4" />
                      </button>
                    </td>"""

# Let's actually add the dropdown state for real rows
# Actually, since it's a table, we can just let the MoreVertical button open the drawer for simplicity, or we can build a small dropdown.
# The user wants "Actions - Dropdown menu (⋮ icon) with: View Profile, Edit Details, Print QR Code, Suspend/Activate, Archive, Delete"
# Let's add a state to track the active dropdown row
state_search = r"const \[page, setPage\] = useState\(1\);"
state_replace = r"const [page, setPage] = useState(1);\n  const [activeDropdown, setActiveDropdown] = useState(null);"
content = re.sub(state_search, state_replace, content)

dropdown_replace_full = r"""<td className="px-4 text-right relative">
                      <button 
                        className="p-1.5 text-slate-400 hover:text-slate-700 rounded-md hover:bg-slate-100 transition-colors opacity-0 group-hover:opacity-100 focus:opacity-100"
                        onClick={(e) => {
                          e.stopPropagation();
                          setActiveDropdown(activeDropdown === driver.id ? null : driver.id);
                        }}
                      >
                        <MoreVertical className="w-4 h-4" />
                      </button>
                      
                      {activeDropdown === driver.id && (
                        <div className="absolute right-8 top-10 w-48 bg-white rounded-lg shadow-lg border border-slate-200 z-50 py-1" onClick={e => e.stopPropagation()}>
                          <button onClick={() => { setActiveDropdown(null); openDriverDrawer(driver); }} className="w-full text-left px-4 py-2 text-sm text-slate-700 hover:bg-slate-50">View Profile</button>
                          <button onClick={() => { setActiveDropdown(null); setFormOpen(true); }} className="w-full text-left px-4 py-2 text-sm text-slate-700 hover:bg-slate-50">Edit Details</button>
                          <button onClick={() => setActiveDropdown(null)} className="w-full text-left px-4 py-2 text-sm text-slate-700 hover:bg-slate-50">Print QR Code</button>
                          <button onClick={() => setActiveDropdown(null)} className="w-full text-left px-4 py-2 text-sm text-slate-700 hover:bg-slate-50">{driver.status === 'Active' ? 'Suspend' : 'Activate'}</button>
                          <button onClick={() => setActiveDropdown(null)} className="w-full text-left px-4 py-2 text-sm text-slate-700 hover:bg-slate-50">Archive</button>
                          <div className="h-px bg-slate-200 my-1"></div>
                          <button onClick={() => setActiveDropdown(null)} className="w-full text-left px-4 py-2 text-sm text-red-600 hover:bg-red-50 font-medium">Delete</button>
                        </div>
                      )}
                    </td>"""

content = re.sub(dropdown_search, dropdown_replace_full, content)

# To make the dropdown close when clicking outside, we can add a click handler to the main container or window.
# Alternatively, adding a fixed overlay behind the dropdown:
dropdown_overlay_fix = r"""{activeDropdown === driver.id && (
                        <>
                        <div className="fixed inset-0 z-40" onClick={(e) => { e.stopPropagation(); setActiveDropdown(null); }}></div>
                        <div className="absolute right-8 top-10 w-48 bg-white rounded-lg shadow-lg border border-slate-200 z-50 py-1" onClick={e => e.stopPropagation()}>
                          <button onClick={() => { setActiveDropdown(null); openDriverDrawer(driver); }} className="w-full text-left px-4 py-2 text-sm text-slate-700 hover:bg-slate-50">View Profile</button>
                          <button onClick={() => { setActiveDropdown(null); setFormOpen(true); }} className="w-full text-left px-4 py-2 text-sm text-slate-700 hover:bg-slate-50">Edit Details</button>
                          <button onClick={() => setActiveDropdown(null)} className="w-full text-left px-4 py-2 text-sm text-slate-700 hover:bg-slate-50">Print QR Code</button>
                          <button onClick={() => setActiveDropdown(null)} className="w-full text-left px-4 py-2 text-sm text-slate-700 hover:bg-slate-50">{driver.status === 'Active' ? 'Suspend' : 'Activate'}</button>
                          <button onClick={() => setActiveDropdown(null)} className="w-full text-left px-4 py-2 text-sm text-slate-700 hover:bg-slate-50">Archive</button>
                          <div className="h-px bg-slate-200 my-1"></div>
                          <button onClick={() => setActiveDropdown(null)} className="w-full text-left px-4 py-2 text-sm text-red-600 hover:bg-red-50 font-medium">Delete</button>
                        </div>
                        </>
                      )}"""

content = content.replace(
    r"""{activeDropdown === driver.id && (
                        <div className="absolute right-8 top-10 w-48 bg-white rounded-lg shadow-lg border border-slate-200 z-50 py-1" onClick={e => e.stopPropagation()}>
                          <button onClick={() => { setActiveDropdown(null); openDriverDrawer(driver); }} className="w-full text-left px-4 py-2 text-sm text-slate-700 hover:bg-slate-50">View Profile</button>
                          <button onClick={() => { setActiveDropdown(null); setFormOpen(true); }} className="w-full text-left px-4 py-2 text-sm text-slate-700 hover:bg-slate-50">Edit Details</button>
                          <button onClick={() => setActiveDropdown(null)} className="w-full text-left px-4 py-2 text-sm text-slate-700 hover:bg-slate-50">Print QR Code</button>
                          <button onClick={() => setActiveDropdown(null)} className="w-full text-left px-4 py-2 text-sm text-slate-700 hover:bg-slate-50">{driver.status === 'Active' ? 'Suspend' : 'Activate'}</button>
                          <button onClick={() => setActiveDropdown(null)} className="w-full text-left px-4 py-2 text-sm text-slate-700 hover:bg-slate-50">Archive</button>
                          <div className="h-px bg-slate-200 my-1"></div>
                          <button onClick={() => setActiveDropdown(null)} className="w-full text-left px-4 py-2 text-sm text-red-600 hover:bg-red-50 font-medium">Delete</button>
                        </div>
                      )}""",
    dropdown_overlay_fix
)

with open('frontend/src/pages/admin/DriverManagementPage.jsx', 'w') as f:
    f.write(content)
