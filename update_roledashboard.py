with open("frontend/src/pages/RoleDashboard.jsx", "r") as f:
    content = f.read()

header_code = """
        {/* Page Header */}
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6">
          <div>
            <div className="flex items-center gap-1.5 text-[11px] font-medium text-slate-500 mb-1">
              <span>SPTC</span>
              <span className="opacity-50">/</span>
              <span>Operations</span>
              <span className="opacity-50">/</span>
              <span className="font-semibold text-slate-700">Fleet Central</span>
            </div>
            <h1 className="text-2xl font-bold text-slate-900 tracking-tight">Dashboard Overview</h1>
          </div>
        </div>
"""

content = content.replace(
    '<div className="w-full p-5 md:p-7 lg:p-8 xl:p-10 max-w-[1600px] mx-auto">',
    '<div className="w-full p-5 md:p-7 lg:p-8 xl:p-10 max-w-[1600px] mx-auto">' + header_code
)

with open("frontend/src/pages/RoleDashboard.jsx", "w") as f:
    f.write(content)
