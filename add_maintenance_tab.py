import re

with open('frontend/src/pages/admin/UnitManagementPage.jsx', 'r') as f:
    content = f.read()

# Add to tab list
content = content.replace("['Profile', 'Documents', 'Activity Log']", "['Profile', 'Documents', 'Maintenance History', 'Activity Log']")

# Inject Maintenance History tab content
maintenance_tab_content = """
              {drawerTab === 'Maintenance History' && (
                <div className="space-y-4">
                  <div className="flex items-center justify-between mb-4">
                    <h3 className="text-sm font-bold text-slate-900 flex items-center gap-2"><Settings className="w-4 h-4 text-blue-600"/> Maintenance & Reports</h3>
                    <button className="text-sm text-blue-600 font-medium hover:text-blue-700">Add Record</button>
                  </div>
                  <div className="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden">
                    <div className="overflow-x-auto">
                      <table className="w-full text-left">
                        <thead>
                          <tr className="bg-slate-50 border-b border-slate-200">
                            <th className="px-4 py-3 text-xs font-semibold text-slate-600">Date</th>
                            <th className="px-4 py-3 text-xs font-semibold text-slate-600">Type</th>
                            <th className="px-4 py-3 text-xs font-semibold text-slate-600">Description</th>
                            <th className="px-4 py-3 text-xs font-semibold text-slate-600">Cost</th>
                            <th className="px-4 py-3 text-xs font-semibold text-slate-600">Status</th>
                          </tr>
                        </thead>
                        <tbody className="divide-y divide-slate-100 text-sm">
                          <tr className="hover:bg-slate-50/50">
                            <td className="px-4 py-3 text-slate-500 whitespace-nowrap">Oct 12, 2024</td>
                            <td className="px-4 py-3 font-medium text-slate-900">Preventive</td>
                            <td className="px-4 py-3 text-slate-600 max-w-[200px] truncate">Oil change and brake pad replacement</td>
                            <td className="px-4 py-3 text-slate-900 font-medium">₱4,500</td>
                            <td className="px-4 py-3"><span className="inline-flex px-2 py-0.5 rounded-full text-[10px] font-semibold bg-green-50 text-green-700 border border-green-200">Completed</span></td>
                          </tr>
                          <tr className="hover:bg-slate-50/50">
                            <td className="px-4 py-3 text-slate-500 whitespace-nowrap">Sep 05, 2024</td>
                            <td className="px-4 py-3 font-medium text-slate-900">Repair</td>
                            <td className="px-4 py-3 text-slate-600 max-w-[200px] truncate">Aircon cleaning and freon refill</td>
                            <td className="px-4 py-3 text-slate-900 font-medium">₱2,800</td>
                            <td className="px-4 py-3"><span className="inline-flex px-2 py-0.5 rounded-full text-[10px] font-semibold bg-green-50 text-green-700 border border-green-200">Completed</span></td>
                          </tr>
                          <tr className="hover:bg-slate-50/50">
                            <td className="px-4 py-3 text-slate-500 whitespace-nowrap">Aug 18, 2024</td>
                            <td className="px-4 py-3 font-medium text-slate-900">Accident</td>
                            <td className="px-4 py-3 text-slate-600 max-w-[200px] truncate">Minor scratch repair on rear bumper</td>
                            <td className="px-4 py-3 text-slate-900 font-medium">₱3,200</td>
                            <td className="px-4 py-3"><span className="inline-flex px-2 py-0.5 rounded-full text-[10px] font-semibold bg-green-50 text-green-700 border border-green-200">Completed</span></td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>
              )}
"""

content = content.replace("{drawerTab === 'Activity Log' && (", maintenance_tab_content + "{drawerTab === 'Activity Log' && (")

with open('frontend/src/pages/admin/UnitManagementPage.jsx', 'w') as f:
    f.write(content)
