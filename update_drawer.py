import re

with open('frontend/src/pages/admin/DriverManagementPage.jsx', 'r') as f:
    content = f.read()

# ADD QR Modal state
state_search = r"const \[drawerOpen, setDrawerOpen\] = useState\(false\);"
state_replace = r"const [drawerOpen, setDrawerOpen] = useState(false);\n  const [qrModalOpen, setQrModalOpen] = useState(false);"
content = re.sub(state_search, state_replace, content)

# Modify Drawer Header
drawer_header_search = r"\{/\* Drawer Header \*/\}.*?\{/\* Drawer Tabs \*/\}"
drawer_header_replace = r"""{/* Drawer Header */}
            <div className="px-6 py-6 border-b border-slate-200 flex flex-col relative bg-slate-50/50">
              <button onClick={() => setDrawerOpen(false)} className="absolute top-4 right-4 p-2 text-slate-400 hover:text-slate-700 bg-white rounded-full shadow-sm hover:shadow">
                <X className="w-5 h-5" />
              </button>
              
              <div className="flex items-start justify-between gap-5 w-full pr-8">
                <div className="flex items-start gap-5">
                  <div className="relative shrink-0">
                    <img src={selectedDriverData.avatar} alt="Profile" className="w-20 h-20 rounded-full border-4 border-white shadow-sm object-cover" />
                    <div className={`absolute bottom-0 right-0 w-5 h-5 rounded-full border-2 border-white ${selectedDriverData.status === 'Active' ? 'bg-emerald-500' : 'bg-slate-400'}`}></div>
                  </div>
                  <div className="pt-1">
                    <div className="flex items-center gap-3 mb-1">
                      <h2 className="text-2xl font-bold text-slate-900">{selectedDriverData.firstName} {selectedDriverData.lastName}</h2>
                      <StatusBadge status={selectedDriverData.status} />
                    </div>
                    <p className="text-sm text-slate-500 font-medium mb-1">ID: {selectedDriverData.id} • Joined {new Date(selectedDriverData.joinDate).toLocaleDateString()}</p>
                    <p className="text-sm text-slate-600 font-medium mb-4 flex items-center gap-1.5"><Calendar className="w-3.5 h-3.5 text-blue-500"/> Today's Schedule: {selectedDriverData.shift} • {selectedDriverData.route}</p>
                    
                    <div className="flex gap-2">
                      <button className="px-3 py-1.5 bg-blue-50 text-blue-600 rounded-lg text-sm font-semibold hover:bg-blue-100 transition-colors flex items-center gap-1.5">
                        <Edit className="w-4 h-4" /> Edit Profile
                      </button>
                      <button className="px-3 py-1.5 bg-slate-100 text-slate-700 rounded-lg text-sm font-semibold hover:bg-slate-200 transition-colors flex items-center gap-1.5">
                        <Printer className="w-4 h-4" /> QR Code
                      </button>
                    </div>
                  </div>
                </div>

                <div 
                  className="w-24 h-24 bg-white rounded-xl shadow-sm border border-slate-200 p-2 cursor-pointer hover:shadow-md hover:border-blue-300 transition-all group relative shrink-0 hidden sm:block"
                  onClick={() => setQrModalOpen(true)}
                >
                  <img src={`https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=${selectedDriverData.id}`} alt="QR Code" className="w-full h-full object-contain group-hover:opacity-80 transition-opacity" />
                  <div className="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity bg-black/5 rounded-xl">
                    <span className="bg-white text-blue-600 px-2 py-1 rounded text-[10px] font-bold shadow-sm">View</span>
                  </div>
                </div>
              </div>
            </div>

            {/* Drawer Tabs */}"""
content = re.sub(drawer_header_search, drawer_header_replace, content, flags=re.DOTALL)

# Modify Drawer Tabs
content = re.sub(
    r"\['Profile', 'Documents', 'Activity Log'\]",
    "['Overview', 'Documents', 'Schedule', 'Remittances', 'Performance', 'Activity Log']",
    content
)

# Rename Profile to Overview references
content = re.sub(r"setDrawerTab\('Profile'\)", "setDrawerTab('Overview')", content)
content = re.sub(r"drawerTab === 'Profile'", "drawerTab === 'Overview'", content)

# I also need to add back the missing tabs components.
tabs_injection_search = r"\{drawerTab === 'Activity Log' && \("
tabs_injection_replace = r"""{drawerTab === 'Schedule' && (
                <div className="space-y-4">
                  <h3 className="text-sm font-bold text-slate-900 mb-4 flex items-center gap-2"><Calendar className="w-4 h-4 text-blue-600"/> Upcoming Shifts</h3>
                  <div className="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden">
                    <table className="w-full text-left">
                      <thead className="bg-slate-50 text-xs text-slate-500 uppercase">
                        <tr><th className="px-4 py-2">Date</th><th className="px-4 py-2">Shift</th><th className="px-4 py-2">Route</th></tr>
                      </thead>
                      <tbody className="divide-y divide-slate-100 text-sm">
                        <tr><td className="px-4 py-3 font-medium">Tomorrow</td><td className="px-4 py-3 text-slate-600">{selectedDriverData.shift}</td><td className="px-4 py-3">{selectedDriverData.route}</td></tr>
                        <tr><td className="px-4 py-3 font-medium">Oct 12, 2026</td><td className="px-4 py-3 text-slate-600">{selectedDriverData.shift}</td><td className="px-4 py-3">{selectedDriverData.route}</td></tr>
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
              )}
              {drawerTab === 'Activity Log' && ("""
content = re.sub(tabs_injection_search, tabs_injection_replace, content)

# I need to add back the Assignment Card into the Overview (formerly Profile) tab.
contact_card_search = r"\{/\* Contact Card \*/\}.*?\{/\* License Card \*/\}"
contact_card_replace = r"""{/* Contact Card */}
                  <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-5">
                    <h3 className="text-sm font-bold text-slate-900 mb-4 flex items-center gap-2"><User className="w-4 h-4 text-blue-600"/> Contact Information</h3>
                    <div className="grid grid-cols-2 gap-y-4 gap-x-6">
                      <div>
                        <p className="text-xs text-slate-500 mb-1">Phone Number</p>
                        <p className="text-sm font-medium text-slate-900">{selectedDriverData.phone}</p>
                      </div>
                      <div>
                        <p className="text-xs text-slate-500 mb-1">Email Address</p>
                        <p className="text-sm font-medium text-slate-900">{selectedDriverData.email}</p>
                      </div>
                      <div className="col-span-2">
                        <p className="text-xs text-slate-500 mb-1">Address</p>
                        <p className="text-sm font-medium text-slate-900">123 Bonifacio St, Brgy. San Jose, Calamba City, Laguna</p>
                      </div>
                    </div>
                  </div>

                  {/* Current Assignment Card */}
                  <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-5">
                    <h3 className="text-sm font-bold text-slate-900 mb-4 flex items-center gap-2"><Map className="w-4 h-4 text-blue-600"/> Current Assignment</h3>
                    <div className="grid grid-cols-2 gap-y-4 gap-x-6">
                      <div>
                        <p className="text-xs text-slate-500 mb-1">Route</p>
                        <div className="flex items-center gap-2">
                          <MapPin className="w-4 h-4 text-emerald-500" />
                          <p className="text-sm font-semibold text-slate-900">{selectedDriverData.route}</p>
                        </div>
                      </div>
                      <div>
                        <p className="text-xs text-slate-500 mb-1">Shift</p>
                        <div className="flex items-center gap-2">
                          <Clock className="w-4 h-4 text-blue-500" />
                          <p className="text-sm font-medium text-slate-900">{selectedDriverData.shift}</p>
                        </div>
                      </div>
                      <div>
                        <p className="text-xs text-slate-500 mb-1">Assigned Unit</p>
                        <p className="text-sm font-medium text-slate-900">Jeepney J-42 (ABC-1234)</p>
                      </div>
                      <div>
                        <p className="text-xs text-slate-500 mb-1">Boundary Rate</p>
                        <p className="text-sm font-medium text-slate-900">₱800 / day</p>
                      </div>
                    </div>
                  </div>

                  {/* License Card */}"""
content = re.sub(contact_card_search, contact_card_replace, content, flags=re.DOTALL)

# Add the QR Modal rendering just before the closing </div> of the page.
qr_modal_code = r"""{/* QR CODE MODAL */}
      {qrModalOpen && selectedDriverData && (
        <div className="fixed inset-0 z-[200] flex items-center justify-center p-4">
          <div className="absolute inset-0 bg-slate-900/60 backdrop-blur-sm" onClick={() => setQrModalOpen(false)}></div>
          <div className="relative bg-white rounded-2xl shadow-2xl p-8 max-w-sm w-full flex flex-col items-center animate-in zoom-in-95 duration-200">
            <button onClick={() => setQrModalOpen(false)} className="absolute top-4 right-4 p-2 text-slate-400 hover:text-slate-700 bg-white rounded-full hover:bg-slate-100 transition-colors">
              <X className="w-5 h-5" />
            </button>
            <h2 className="text-lg font-bold text-slate-900 mb-1">Driver QR Code</h2>
            <p className="text-sm text-slate-500 mb-6 text-center">Scan this code to view the driver profile or assign a vehicle.</p>
            
            <div className="bg-slate-50 p-4 rounded-xl border border-slate-200 mb-6 w-full flex justify-center">
              <img src={`https://api.qrserver.com/v1/create-qr-code/?size=250x250&data=${selectedDriverData.id}`} alt="QR Code Large" className="w-48 h-48 mix-blend-multiply" />
            </div>
            
            <div className="text-center w-full">
              <p className="font-bold text-slate-900 text-lg">{selectedDriverData.firstName} {selectedDriverData.lastName}</p>
              <p className="text-sm text-slate-500 font-mono mt-1">{selectedDriverData.id}</p>
            </div>
            
            <button 
              className="mt-6 w-full flex items-center justify-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700 transition-colors"
              onClick={() => {
                alert("Downloading QR Code...");
              }}
            >
              <Download className="w-4 h-4" /> Download PNG
            </button>
          </div>
        </div>
      )}"""
content = re.sub(r"\{/\* ADD DRIVER FORM MODAL \*/\}", qr_modal_code + "\n\n      {/* ADD DRIVER FORM MODAL */}", content)

with open('frontend/src/pages/admin/DriverManagementPage.jsx', 'w') as f:
    f.write(content)
