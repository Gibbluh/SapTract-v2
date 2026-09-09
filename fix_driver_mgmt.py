import re

with open('frontend/src/pages/admin/DriverManagementPage.jsx', 'r') as f:
    content = f.read()

# 1. Update Tabs in Header
content = re.sub(
    r"\['All Drivers', 'Active', 'Suspended', 'Inactive', 'Documents Expiring', 'Archived'\]",
    "['All Drivers', 'Active', 'Suspended', 'Inactive', 'Documents Expiring']",
    content
)

# 2. Update Table Headers
table_header_search = r'<th className="px-4 py-3 text-xs font-semibold text-slate-600 uppercase tracking-wider">Assignment</th>\s*<th className="px-4 py-3 text-xs font-semibold text-slate-600 uppercase tracking-wider">Status</th>\s*<th className="px-4 py-3 text-xs font-semibold text-slate-600 uppercase tracking-wider">Performance</th>\s*<th className="px-4 py-3 text-xs font-semibold text-slate-600 uppercase tracking-wider text-right">Total Remitted</th>'
table_header_replace = r'<th className="px-4 py-3 text-xs font-semibold text-slate-600 uppercase tracking-wider">Status</th>\n                  <th className="px-4 py-3 text-xs font-semibold text-slate-600 uppercase tracking-wider">Date Joined</th>'
content = re.sub(table_header_search, table_header_replace, content)

# 3. Update Table Body Cells
table_body_search = r'<td className="px-4">\s*<div className="flex items-center gap-1.5 mb-0.5">\s*<MapPin className="w-3.5 h-3.5 text-slate-400" />\s*<span className="text-sm font-medium text-slate-700">\{driver.route\}</span>\s*</div>\s*<div className="flex items-center gap-1.5">\s*<Clock className="w-3.5 h-3.5 text-slate-400" />\s*<span className="text-xs text-slate-500">\{driver.shift\}</span>\s*</div>\s*</td>\s*<td className="px-4">\s*<StatusBadge status=\{driver.status\} />\s*</td>\s*<td className="px-4">\s*<div className="flex items-center gap-2">\s*<span className="text-sm font-semibold text-slate-700 flex items-center gap-1">\s*\{driver.rating\} <Star className="w-3 h-3 fill-amber-400 text-amber-400" />\s*</span>\s*<div className="w-16 h-1.5 bg-slate-100 rounded-full overflow-hidden">\s*<div className="h-full bg-blue-500 rounded-full" style=\{\{ width: `\$\{\(driver.rating / 5\) \* 100\}%` \}\}></div>\s*</div>\s*</div>\s*</td>\s*<td className="px-4 text-right">\s*<div className="text-sm font-bold text-slate-900">₱\{driver.remittances.toLocaleString\(\)\}</div>\s*<div className="text-xs text-slate-500">Lifetime</div>\s*</td>'
table_body_replace = r'<td className="px-4">\n                      <StatusBadge status={driver.status} />\n                    </td>\n                    <td className="px-4">\n                      <div className="text-sm text-slate-700">{new Date(driver.joinDate).toLocaleDateString()}</div>\n                    </td>'
content = re.sub(table_body_search, table_body_replace, content)

# 4. Update Drawer Tabs array
content = re.sub(
    r"\['Overview', 'Documents', 'Schedule', 'Remittances', 'Performance'\]",
    "['Profile', 'Documents', 'Activity Log']",
    content
)

# 5. Fix drawer tab states
content = re.sub(r"setDrawerTab\('Overview'\)", "setDrawerTab('Profile')", content)
content = re.sub(r"drawerTab === 'Overview'", "drawerTab === 'Profile'", content)
content = re.sub(r"drawerTab !== 'Overview'", "drawerTab !== 'Profile'", content)

# 6. Remove Drawer Schedule, Remittances, Performance sections, add Activity Log
drawer_tabs_search = r"\{drawerTab === 'Schedule' && \(.*?\s*\}\s*\{drawerTab === 'Remittances' && \(.*?\s*\}\s*\{drawerTab === 'Performance' && \(.*?\s*\}"
drawer_tabs_replace = r"""{drawerTab === 'Activity Log' && (
                <div className="space-y-4">
                  <h3 className="text-sm font-bold text-slate-900 mb-4 flex items-center gap-2"><Calendar className="w-4 h-4 text-blue-600"/> Recent Activity</h3>
                  <div className="bg-white rounded-xl border border-slate-200 shadow-sm p-5">
                    <div className="relative border-l-2 border-slate-200 ml-3 space-y-6 pb-4">
                      <div className="relative">
                        <div className="absolute -left-[21px] bg-blue-100 p-1 rounded-full border-2 border-white"><CheckCircle className="w-4 h-4 text-blue-600" /></div>
                        <div className="pl-6">
                          <p className="text-sm font-medium text-slate-900">Profile Updated</p>
                          <p className="text-xs text-slate-500">Address information was updated by Super Admin</p>
                          <p className="text-[10px] text-slate-400 mt-1">Today, 10:30 AM</p>
                        </div>
                      </div>
                      <div className="relative">
                        <div className="absolute -left-[21px] bg-emerald-100 p-1 rounded-full border-2 border-white"><FileText className="w-4 h-4 text-emerald-600" /></div>
                        <div className="pl-6">
                          <p className="text-sm font-medium text-slate-900">Document Uploaded</p>
                          <p className="text-xs text-slate-500">New Medical Certificate was uploaded</p>
                          <p className="text-[10px] text-slate-400 mt-1">Oct 12, 2026, 2:15 PM</p>
                        </div>
                      </div>
                      <div className="relative">
                        <div className="absolute -left-[21px] bg-amber-100 p-1 rounded-full border-2 border-white"><Star className="w-4 h-4 text-amber-600" /></div>
                        <div className="pl-6">
                          <p className="text-sm font-medium text-slate-900">Status Changed</p>
                          <p className="text-xs text-slate-500">Status changed from On Leave to Active</p>
                          <p className="text-[10px] text-slate-400 mt-1">Oct 01, 2026, 9:00 AM</p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              )}"""
content = re.sub(drawer_tabs_search, drawer_tabs_replace, content, flags=re.DOTALL)

# 7. Remove current assignment from Drawer Overview (Profile)
assignment_card_search = r"\{/\* Assignment Card \*/\}.*?\{/\* License Card \*/\}"
assignment_card_replace = r"{/* License Card */}"
content = re.sub(assignment_card_search, assignment_card_replace, content, flags=re.DOTALL)

# 8. Remove Route/Shift from Add Form
route_shift_search = r"\{/\* Section 3 \*/\}.*?\{/\* Modal Footer \*/\}"
route_shift_replace = r"""{/* Section 3 */}
                  <section>
                    <h3 className="text-sm font-bold text-slate-900 mb-4 uppercase tracking-wider pb-2 border-b border-slate-200">Cooperative Details</h3>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                      <div>
                        <label className="block text-xs font-semibold text-slate-700 mb-1">Member ID</label>
                        <input type="text" className="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none" placeholder="e.g. COOP-1001" />
                      </div>
                      <div>
                        <label className="block text-xs font-semibold text-slate-700 mb-1">Date Joined</label>
                        <input type="date" className="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none" />
                      </div>
                      <div>
                        <label className="block text-xs font-semibold text-slate-700 mb-1">Status</label>
                        <select className="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none bg-white">
                          <option>Active</option>
                          <option>On Leave</option>
                          <option>Suspended</option>
                          <option>Inactive</option>
                        </select>
                      </div>
                      <div>
                        <label className="block text-xs font-semibold text-slate-700 mb-1">Boundary Rate (₱)</label>
                        <input type="number" className="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none" placeholder="e.g. 800" />
                      </div>
                    </div>
                  </section>
                  {/* Section 4 */}
                  <section>
                    <h3 className="text-sm font-bold text-slate-900 mb-4 uppercase tracking-wider pb-2 border-b border-slate-200">Emergency Contact</h3>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                      <div>
                        <label className="block text-xs font-semibold text-slate-700 mb-1">Contact Name *</label>
                        <input type="text" className="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none" placeholder="Full Name" />
                      </div>
                      <div>
                        <label className="block text-xs font-semibold text-slate-700 mb-1">Relationship</label>
                        <select className="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none bg-white">
                          <option>Spouse</option>
                          <option>Parent</option>
                          <option>Sibling</option>
                          <option>Child</option>
                          <option>Other</option>
                        </select>
                      </div>
                      <div className="md:col-span-2">
                        <label className="block text-xs font-semibold text-slate-700 mb-1">Contact Number *</label>
                        <input type="text" className="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none" placeholder="09XX XXX XXXX" />
                      </div>
                    </div>
                  </section>
                </div>
              </div>
            </div>

            {/* Modal Footer */}"""
content = re.sub(route_shift_search, route_shift_replace, content, flags=re.DOTALL)

with open('frontend/src/pages/admin/DriverManagementPage.jsx', 'w') as f:
    f.write(content)
