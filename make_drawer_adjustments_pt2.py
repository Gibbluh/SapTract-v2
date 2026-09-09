import re

with open('frontend/src/pages/admin/DriverManagementPage.jsx', 'r') as f:
    content = f.read()

# 1. Remove "Today's Schedule: " string
schedule_search = r"<Calendar className=\"w-3\.5 h-3\.5 text-blue-500\"/> Today's Schedule: \{new Date\(\)\.toLocaleDateString\(\)\}"
schedule_replace = r"""<Calendar className="w-3.5 h-3.5 text-blue-500"/> {new Date().toLocaleDateString()}"""
content = re.sub(schedule_search, schedule_replace, content)

# 2. Add Upload Document button to Documents tab
documents_search = r"<h3 className=\"text-sm font-bold text-slate-900 mb-4 flex items-center gap-2\"><FileText className=\"w-4 h-4 text-blue-600\"/> Uploaded Documents</h3>"
documents_replace = r"""<div className="flex justify-between items-center mb-4">
                    <h3 className="text-sm font-bold text-slate-900 flex items-center gap-2"><FileText className="w-4 h-4 text-blue-600"/> Uploaded Documents</h3>
                    <button className="flex items-center gap-1.5 px-3 py-1.5 bg-blue-50 text-blue-600 hover:bg-blue-100 rounded-lg text-xs font-semibold transition-colors">
                      <Upload className="w-3.5 h-3.5" /> Upload Document
                    </button>
                  </div>"""
content = re.sub(documents_search, documents_replace, content)

# 3. Combine Remittances and Transactions (Remove Remittances)
tabs_array_search = r"\['Overview', 'Documents', 'Schedule', 'Remittances', 'Transactions', 'Activity Log'\]"
tabs_array_replace = r"['Overview', 'Documents', 'Schedule', 'Transactions', 'Activity Log']"
content = re.sub(tabs_array_search, tabs_array_replace, content)

remittances_content_search = r"\{drawerTab === 'Remittances' && \(\s*<div className=\"space-y-4\">\s*<h3 className=\"text-sm font-bold text-slate-900 mb-4 flex items-center gap-2\"><CheckCircle className=\"w-4 h-4 text-blue-600\"/> Recent Remittances</h3>.*?</div>\s*\)\}"
remittances_content_replace = r""
content = re.sub(remittances_content_search, remittances_content_replace, content, flags=re.DOTALL)

with open('frontend/src/pages/admin/DriverManagementPage.jsx', 'w') as f:
    f.write(content)
