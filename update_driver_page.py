import re

with open('frontend/src/pages/admin/DriverManagementPage.jsx', 'r') as f:
    content = f.read()

# 1. Remove the Driver Management badge
content = re.sub(
    r'<h1 className="text-2xl font-bold text-slate-900 flex items-center gap-2">\s*Drivers Management\s*<span className="bg-blue-100 text-blue-700 text-xs font-bold px-2 py-0.5 rounded-full">\{MOCK_DRIVERS\.length\}</span>\s*</h1>',
    '<h1 className="text-2xl font-bold text-slate-900 flex items-center gap-2">Drivers Management</h1>',
    content
)

# 2. Fix the Search Driver input
content = content.replace(
    'className="pl-9 pr-4 py-2 border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none w-64 transition-all"',
    'className="pl-9 pr-4 py-2 border border-slate-300 dark:border-slate-600 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none w-64 transition-all bg-white dark:bg-slate-800 text-slate-900 dark:text-white placeholder:text-slate-400"'
)

# 3. Replace the placeholder for tabs
tabs_replacement = """              {drawerTab === 'Documents' && (
                <div className="space-y-4">
                  <h3 className="text-sm font-bold text-slate-900 mb-4 flex items-center gap-2"><FileText className="w-4 h-4 text-blue-600"/> Uploaded Documents</h3>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    {[
                      { name: 'Professional Driver\\'s License', status: 'Valid', expiry: selectedDriverData.licenseExpiry, color: 'emerald' },
                      { name: 'Medical Certificate', status: 'Valid', expiry: '2027-05-15', color: 'emerald' },
                      { name: 'NBI Clearance', status: 'Expiring Soon', expiry: '2026-10-01', color: 'amber' }
                    ].map((doc, i) => (
                      <div key={i} className="bg-white p-4 rounded-xl border border-slate-200 shadow-sm flex flex-col">
                        <div className="flex justify-between items-start mb-3">
                          <FileText className={`w-8 h-8 text-${doc.color}-500 bg-${doc.color}-50 p-1.5 rounded-lg`} />
                          <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full bg-${doc.color}-100 text-${doc.color}-700`}>{doc.status}</span>
                        </div>
                        <p className="font-semibold text-slate-900 text-sm mb-1">{doc.name}</p>
                        <p className="text-xs text-slate-500">Expires: {new Date(doc.expiry).toLocaleDateString()}</p>
                        <button className="mt-3 text-xs font-medium text-blue-600 hover:text-blue-800 text-left">View Document</button>
                      </div>
                    ))}
                  </div>
                </div>
              )}
              {drawerTab === 'Schedule' && (
                <div className="space-y-4">
                  <h3 className="text-sm font-bold text-slate-900 mb-4 flex items-center gap-2"><Calendar className="w-4 h-4 text-blue-600"/> Upcoming Shifts</h3>
                  <div className="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden">
                    <table className="w-full text-left">
                      <thead className="bg-slate-50 text-xs text-slate-500 uppercase">
                        <tr><th className="px-4 py-2">Date</th><th className="px-4 py-2">Shift</th><th className="px-4 py-2">Route</th></tr>
                      </thead>
                      <tbody className="divide-y divide-slate-100 text-sm">
                        <tr><td className="px-4 py-3 font-medium">Tomorrow</td><td className="px-4 py-3 text-slate-600">06:00 AM - 02:00 PM</td><td className="px-4 py-3">{selectedDriverData.route}</td></tr>
                        <tr><td className="px-4 py-3 font-medium">Oct 12, 2026</td><td className="px-4 py-3 text-slate-600">06:00 AM - 02:00 PM</td><td className="px-4 py-3">{selectedDriverData.route}</td></tr>
                        <tr><td className="px-4 py-3 font-medium">Oct 13, 2026</td><td className="px-4 py-3 text-slate-600">Day Off</td><td className="px-4 py-3 text-slate-400">-</td></tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              )}
              {drawerTab === 'Remittances' && (
                <div className="space-y-4">
                  <h3 className="text-sm font-bold text-slate-900 mb-4 flex items-center gap-2"><CheckCircle className="w-4 h-4 text-blue-600"/> Recent Remittances</h3>
                  <div className="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden">
                    <table className="w-full text-left">
                      <thead className="bg-slate-50 text-xs text-slate-500 uppercase">
                        <tr><th className="px-4 py-2">Date</th><th className="px-4 py-2">Amount</th><th className="px-4 py-2">Status</th></tr>
                      </thead>
                      <tbody className="divide-y divide-slate-100 text-sm">
                        <tr><td className="px-4 py-3">Today, 2:30 PM</td><td className="px-4 py-3 font-bold text-slate-900">₱800.00</td><td className="px-4 py-3"><span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-700">Cleared</span></td></tr>
                        <tr><td className="px-4 py-3">Yesterday</td><td className="px-4 py-3 font-bold text-slate-900">₱800.00</td><td className="px-4 py-3"><span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-700">Cleared</span></td></tr>
                        <tr><td className="px-4 py-3">Oct 09, 2026</td><td className="px-4 py-3 font-bold text-slate-900">₱800.00</td><td className="px-4 py-3"><span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-700">Cleared</span></td></tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              )}
              {drawerTab === 'Performance' && (
                <div className="space-y-4">
                  <h3 className="text-sm font-bold text-slate-900 mb-4 flex items-center gap-2"><Star className="w-4 h-4 text-blue-600"/> Performance Metrics</h3>
                  <div className="grid grid-cols-2 gap-4">
                    <div className="bg-white p-4 rounded-xl border border-slate-200 shadow-sm text-center">
                      <p className="text-xs text-slate-500 mb-1">Current Rating</p>
                      <p className="text-3xl font-bold text-slate-900 flex items-center justify-center gap-2">{selectedDriverData.rating} <Star className="w-6 h-6 fill-amber-400 text-amber-400"/></p>
                    </div>
                    <div className="bg-white p-4 rounded-xl border border-slate-200 shadow-sm text-center">
                      <p className="text-xs text-slate-500 mb-1">Trips Completed (Month)</p>
                      <p className="text-3xl font-bold text-slate-900">142</p>
                    </div>
                    <div className="bg-white p-4 rounded-xl border border-slate-200 shadow-sm text-center">
                      <p className="text-xs text-slate-500 mb-1">Incident Reports</p>
                      <p className="text-3xl font-bold text-emerald-600">0</p>
                    </div>
                    <div className="bg-white p-4 rounded-xl border border-slate-200 shadow-sm text-center">
                      <p className="text-xs text-slate-500 mb-1">Punctuality</p>
                      <p className="text-3xl font-bold text-slate-900">98%</p>
                    </div>
                  </div>
                </div>
              )}"""

content = re.sub(
    r"\{\s*drawerTab !== 'Overview' && \(\s*<div className=\"flex flex-col items-center justify-center h-64 text-slate-400\">\s*<LayoutGrid className=\"w-12 h-12 mb-3 opacity-20\" />\s*<p>Module content for \{drawerTab\} will appear here.</p>\s*</div>\s*\)\s*\}",
    tabs_replacement,
    content,
    flags=re.DOTALL
)

with open('frontend/src/pages/admin/DriverManagementPage.jsx', 'w') as f:
    f.write(content)
