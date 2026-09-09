import re

with open("frontend/src/pages/admin/components/AddUnitModal.jsx", "r") as f:
    content = f.read()

# Make it max-w-4xl
content = content.replace("max-w-5xl", "max-w-4xl")

# Fix button
content = content.replace(
"""            <button 
              type="button" 
              onClick={(e) => handleSubmit(e, true)}
              disabled={isSubmitting}
              className="px-4 py-2 text-sm font-semibold text-slate-700 border border-slate-300 rounded-lg hover:bg-slate-50 transition-colors"
            >
              Save & Add Another
            </button>""",
"""            <button 
              type="button" 
              className="px-4 py-2 text-sm font-semibold text-slate-700 border border-slate-300 rounded-lg hover:bg-slate-50 transition-colors"
            >
              Save as Draft
            </button>""")


with open("frontend/src/pages/admin/components/AddUnitModal.jsx", "w") as f:
    f.write(content)
