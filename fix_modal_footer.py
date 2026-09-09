import re

with open('frontend/src/pages/admin/DriverManagementPage.jsx', 'r') as f:
    content = f.read()

# Replace the closing div of the form to </form>
footer_search = r"\{/\* Modal Footer \*/\}.*?Cancel</button>\s*<div className=\"flex gap-3\">\s*<button className=\"px-4 py-2 text-sm font-semibold text-slate-700 border border-slate-300 rounded-lg hover:bg-slate-50 transition-colors\">Save as Draft</button>\s*<button className=\"px-5 py-2 text-sm font-bold text-white bg-blue-600 rounded-lg hover:bg-blue-700 transition-colors shadow-sm flex items-center gap-2\">\s*<Check className=\"w-4 h-4\" /> Save Driver\s*</button>\s*</div>\s*</div>\s*</div>\s*</div>\s*\)"

footer_replace = r"""{/* Modal Footer */}
            <div className="px-6 py-4 border-t border-slate-200 bg-white flex justify-between items-center">
              <button type="button" onClick={() => setFormOpen(false)} className="px-4 py-2 text-sm font-semibold text-slate-600 hover:text-slate-900 transition-colors">Cancel</button>
              <div className="flex gap-3">
                <button type="button" className="px-4 py-2 text-sm font-semibold text-slate-700 border border-slate-300 rounded-lg hover:bg-slate-50 transition-colors">Save as Draft</button>
                <button type="submit" className="px-5 py-2 text-sm font-bold text-white bg-blue-600 rounded-lg hover:bg-blue-700 transition-colors shadow-sm flex items-center gap-2">
                  <Check className="w-4 h-4" /> Save Driver
                </button>
              </div>
            </div>
          </form>
        </div>
      )"""

content = re.sub(footer_search, footer_replace, content, flags=re.DOTALL)

with open('frontend/src/pages/admin/DriverManagementPage.jsx', 'w') as f:
    f.write(content)
