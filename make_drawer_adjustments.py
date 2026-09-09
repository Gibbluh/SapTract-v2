import re

with open('frontend/src/pages/admin/DriverManagementPage.jsx', 'r') as f:
    content = f.read()

# 1. Update Today's Schedule to include date and time range
schedule_search = r"<p className=\"text-sm text-slate-600 font-medium mb-4 flex items-center gap-1.5\"><Calendar className=\"w-3.5 h-3.5 text-blue-500\"/> Today's Schedule: \{selectedDriverData.shift\} • \{selectedDriverData.route\}</p>"
schedule_replace = r"""<p className="text-sm text-slate-600 font-medium mb-4 flex items-center gap-1.5"><Calendar className="w-3.5 h-3.5 text-blue-500"/> Today's Schedule: {new Date().toLocaleDateString()} • {selectedDriverData.shift === 'First Shift' ? '06:00 AM - 02:00 PM' : selectedDriverData.shift === 'Second Shift' ? '02:00 PM - 10:00 PM' : '08:00 AM - 05:00 PM'} • {selectedDriverData.route}</p>"""
content = re.sub(schedule_search, schedule_replace, content)

# 2. Add margin right to QR code to pull it left
qr_code_container_search = r'className="w-24 h-24 bg-white rounded-xl shadow-sm border border-slate-200 p-2 cursor-pointer hover:shadow-md hover:border-blue-300 transition-all group relative shrink-0 hidden sm:block"'
qr_code_container_replace = r'className="w-24 h-24 bg-white rounded-xl shadow-sm border border-slate-200 p-2 cursor-pointer hover:shadow-md hover:border-blue-300 transition-all group relative shrink-0 hidden sm:block mr-12"'
content = re.sub(qr_code_container_search, qr_code_container_replace, content)

# 3. Replace Performance tab with Transactions
tabs_array_search = r"\['Overview', 'Documents', 'Schedule', 'Remittances', 'Performance', 'Activity Log'\]"
tabs_array_replace = r"['Overview', 'Documents', 'Schedule', 'Remittances', 'Transactions', 'Activity Log']"
content = re.sub(tabs_array_search, tabs_array_replace, content)

performance_content_search = r"\{drawerTab === 'Performance' && \(\s*<div className=\"space-y-4\">\s*<h3 className=\"text-sm font-bold text-slate-900 mb-4 flex items-center gap-2\"><Star className=\"w-4 h-4 text-blue-600\"/> Performance Metrics</h3>.*?</div>\s*\)\}"
performance_content_replace = r"""{drawerTab === 'Transactions' && (
                <div className="space-y-4">
                  <h3 className="text-sm font-bold text-slate-900 mb-4 flex items-center gap-2"><FileText className="w-4 h-4 text-blue-600"/> Transaction History</h3>
                  <div className="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden">
                    <table className="w-full text-left">
                      <thead className="bg-slate-50 text-xs text-slate-500 uppercase">
                        <tr><th className="px-4 py-2">Date</th><th className="px-4 py-2">Description</th><th className="px-4 py-2">Amount</th><th className="px-4 py-2">Status</th></tr>
                      </thead>
                      <tbody className="divide-y divide-slate-100 text-sm">
                        <tr><td className="px-4 py-3">Today, 10:00 AM</td><td className="px-4 py-3 text-slate-700">Fuel Advance</td><td className="px-4 py-3 font-bold text-red-600">-₱500.00</td><td className="px-4 py-3"><span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-slate-100 text-slate-700">Deducted</span></td></tr>
                        <tr><td className="px-4 py-3">Yesterday, 3:15 PM</td><td className="px-4 py-3 text-slate-700">Daily Remittance</td><td className="px-4 py-3 font-bold text-emerald-600">+₱800.00</td><td className="px-4 py-3"><span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-700">Cleared</span></td></tr>
                        <tr><td className="px-4 py-3">Oct 09, 2026</td><td className="px-4 py-3 text-slate-700">Maintenance Fee</td><td className="px-4 py-3 font-bold text-red-600">-₱150.00</td><td className="px-4 py-3"><span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-slate-100 text-slate-700">Deducted</span></td></tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              )}"""

content = re.sub(performance_content_search, performance_content_replace, content, flags=re.DOTALL)

with open('frontend/src/pages/admin/DriverManagementPage.jsx', 'w') as f:
    f.write(content)
