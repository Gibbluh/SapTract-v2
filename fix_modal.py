import re

with open('frontend/src/pages/admin/DriverManagementPage.jsx', 'r') as f:
    content = f.read()

# 1. Update the modal container and add a form tag
modal_search = r"\{/\* ADD DRIVER FORM MODAL \*/\}\s*\{formOpen && \(\s*<div className=\"fixed inset-0 z-\[100\] flex items-center justify-center p-4 sm:p-6\">\s*<div className=\"absolute inset-0 bg-slate-900/40 backdrop-blur-sm\" onClick=\{\(\) => setFormOpen\(false\)\}></div>\s*<div className=\"relative w-full max-w-4xl bg-white rounded-2xl shadow-2xl flex flex-col max-h-full overflow-hidden animate-in zoom-in-95 duration-200\">"
modal_replace = r"""{/* ADD DRIVER FORM MODAL */}
      {formOpen && (
        <div className="fixed inset-0 z-[100] flex items-center justify-center p-4 sm:p-6">
          <div className="absolute inset-0 bg-slate-900/40 backdrop-blur-sm" onClick={() => setFormOpen(false)}></div>
          <form onSubmit={(e) => { e.preventDefault(); setFormOpen(false); }} className="relative w-full max-w-5xl bg-white rounded-2xl shadow-2xl flex flex-col max-h-[85vh] overflow-hidden animate-in zoom-in-95 duration-200">"""
content = re.sub(modal_search, modal_replace, content)

# 2. Fix the Modal Footer to use type="submit" for Save Driver
footer_search = r"\{/\* Modal Footer \*/\}\s*<div className=\"px-6 py-4 border-t border-slate-200 bg-slate-50 flex justify-between items-center\">\s*<button onClick=\{\(\) => setFormOpen\(false\)\} className=\"px-4 py-2 text-sm font-medium text-slate-700 hover:text-slate-900 transition-colors\">\s*Cancel\s*</button>\s*<div className=\"flex gap-3\">\s*<button className=\"px-4 py-2 border border-slate-300 rounded-lg text-sm font-medium text-slate-700 hover:bg-slate-50 transition-colors\">\s*Save as Draft\s*</button>\s*<button className=\"px-4 py-2 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700 transition-colors shadow-sm flex items-center gap-2\">\s*<Check className=\"w-4 h-4\" /> Save Driver\s*</button>\s*</div>\s*</div>\s*</div>\s*</div>\s*\)"
# Actually, the footer background is white now, wait let's just match dynamically
footer_search = r"\{/\* Modal Footer \*/\}.*?Cancel\s*</button>\s*<div className=\"flex gap-3\">\s*<button className=\"px-4 py-2 border border-slate-300 rounded-lg text-sm font-medium text-slate-700 hover:bg-slate-50 transition-colors\">\s*Save as Draft\s*</button>\s*<button className=\"px-4 py-2 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700 transition-colors shadow-sm flex items-center gap-2\">\s*<Check className=\"w-4 h-4\" /> Save Driver\s*</button>\s*</div>\s*</div>\s*</div>\s*</div>\s*\)"
footer_replace = r"""{/* Modal Footer */}
            <div className="px-6 py-4 border-t border-slate-200 bg-white flex justify-between items-center shrink-0">
              <button type="button" onClick={() => setFormOpen(false)} className="px-4 py-2 text-sm font-medium text-slate-700 hover:text-slate-900 transition-colors">
                Cancel
              </button>
              <div className="flex gap-3">
                <button type="button" className="px-4 py-2 border border-slate-300 rounded-lg text-sm font-medium text-slate-700 hover:bg-slate-50 transition-colors">
                  Save as Draft
                </button>
                <button type="submit" className="px-4 py-2 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700 transition-colors shadow-sm flex items-center gap-2">
                  <Check className="w-4 h-4" /> Save Driver
                </button>
              </div>
            </div>
          </form>
        </div>
      )"""
content = re.sub(footer_search, footer_replace, content, flags=re.DOTALL)

# 3. Replace the Form Fields Col
form_fields_search = r"\{/\* Form Fields Col \*/\}.*?\{/\* Modal Footer \*/\}"
form_fields_replace = r"""{/* Form Fields Col */}
                <div className="lg:col-span-9 space-y-8">
                  {/* Section 1 */}
                  <section>
                    <h3 className="text-sm font-bold text-slate-900 mb-4 uppercase tracking-wider pb-2 border-b border-slate-200">Personal Information</h3>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                      <div>
                        <label className="block text-xs font-semibold text-slate-700 mb-1">First Name *</label>
                        <input required type="text" className="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none bg-white text-slate-900" placeholder="e.g. Juan" />
                      </div>
                      <div>
                        <label className="block text-xs font-semibold text-slate-700 mb-1">Last Name *</label>
                        <input required type="text" className="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none bg-white text-slate-900" placeholder="e.g. Dela Cruz" />
                      </div>
                      <div>
                        <label className="block text-xs font-semibold text-slate-700 mb-1">Phone Number *</label>
                        <div className="flex">
                          <span className="inline-flex items-center px-3 border border-r-0 border-slate-300 rounded-l-lg bg-slate-50 text-slate-500 text-sm font-medium">+63</span>
                          <input required type="tel" pattern="[0-9]{10}" title="10 digit phone number after +63" className="flex-1 px-3 py-2 border border-slate-300 rounded-r-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none bg-white text-slate-900" placeholder="912 345 6789" />
                        </div>
                      </div>
                      <div>
                        <label className="block text-xs font-semibold text-slate-700 mb-1">Email Address</label>
                        <input type="email" className="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none bg-white text-slate-900" placeholder="juan@example.com" />
                      </div>
                      <div className="md:col-span-2">
                        <label className="block text-xs font-semibold text-slate-700 mb-1">Complete Address *</label>
                        <textarea required className="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none resize-none bg-white text-slate-900" rows="2" placeholder="House/Block No., Street, Barangay, City, Province"></textarea>
                      </div>
                    </div>
                  </section>

                  {/* Section 2 */}
                  <section>
                    <h3 className="text-sm font-bold text-slate-900 mb-4 uppercase tracking-wider pb-2 border-b border-slate-200">License Information</h3>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                      <div>
                        <label className="block text-xs font-semibold text-slate-700 mb-1">License Number *</label>
                        <input required type="text" className="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm font-mono focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none uppercase bg-white text-slate-900" placeholder="N00-00-000000" />
                      </div>
                      <div>
                        <label className="block text-xs font-semibold text-slate-700 mb-1">License Type *</label>
                        <select required className="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none bg-white text-slate-900">
                          <option value="">Select Type</option>
                          <option value="Professional">Professional</option>
                          <option value="Non-Professional">Non-Professional</option>
                        </select>
                      </div>
                      <div>
                        <label className="block text-xs font-semibold text-slate-700 mb-1">Expiry Date *</label>
                        <input required type="date" className="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none bg-white text-slate-900" />
                      </div>
                    </div>
                  </section>

                  {/* Section 3 */}
                  <section>
                    <h3 className="text-sm font-bold text-slate-900 mb-4 uppercase tracking-wider pb-2 border-b border-slate-200">Cooperative Details</h3>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                      <div>
                        <label className="block text-xs font-semibold text-slate-700 mb-1">Member ID</label>
                        <input type="text" className="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none bg-white text-slate-900" placeholder="e.g. COOP-1001" />
                      </div>
                      <div>
                        <label className="block text-xs font-semibold text-slate-700 mb-1">Date Joined</label>
                        <input type="date" className="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none bg-white text-slate-900" />
                      </div>
                      <div>
                        <label className="block text-xs font-semibold text-slate-700 mb-1">Status</label>
                        <select className="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none bg-white text-slate-900">
                          <option>Active</option>
                          <option>On Leave</option>
                          <option>Suspended</option>
                          <option>Inactive</option>
                        </select>
                      </div>
                      <div>
                        <label className="block text-xs font-semibold text-slate-700 mb-1">Boundary Rate (₱)</label>
                        <input type="number" min="0" step="10" className="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none bg-white text-slate-900" placeholder="e.g. 800" />
                      </div>
                    </div>
                  </section>
                  {/* Section 4 */}
                  <section>
                    <h3 className="text-sm font-bold text-slate-900 mb-4 uppercase tracking-wider pb-2 border-b border-slate-200">Emergency Contact</h3>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                      <div>
                        <label className="block text-xs font-semibold text-slate-700 mb-1">Contact Name *</label>
                        <input required type="text" className="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none bg-white text-slate-900" placeholder="Full Name" />
                      </div>
                      <div>
                        <label className="block text-xs font-semibold text-slate-700 mb-1">Relationship</label>
                        <select className="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none bg-white text-slate-900">
                          <option>Spouse</option>
                          <option>Parent</option>
                          <option>Sibling</option>
                          <option>Child</option>
                          <option>Other</option>
                        </select>
                      </div>
                      <div className="md:col-span-2">
                        <label className="block text-xs font-semibold text-slate-700 mb-1">Contact Number *</label>
                        <input required type="tel" className="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none bg-white text-slate-900" placeholder="09XX XXX XXXX" />
                      </div>
                    </div>
                  </section>
                </div>
              </div>
            </div>

            {/* Modal Footer */}"""
content = re.sub(form_fields_search, form_fields_replace, content, flags=re.DOTALL)

with open('frontend/src/pages/admin/DriverManagementPage.jsx', 'w') as f:
    f.write(content)
