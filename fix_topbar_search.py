import re

with open("frontend/src/components/layout/Topbar.jsx", "r") as f:
    content = f.read()

# Replace bg-slate-500/10 with bg-white border-slate-300
content = content.replace("bg-slate-500/10 hover:bg-slate-500/20 border border-slate-500/20 text-current opacity-80", "bg-white hover:bg-slate-50 border border-slate-300 text-slate-600 opacity-100")

with open("frontend/src/components/layout/Topbar.jsx", "w") as f:
    f.write(content)
