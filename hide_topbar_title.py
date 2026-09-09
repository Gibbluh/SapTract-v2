import re

with open("frontend/src/components/layout/Topbar.jsx", "r") as f:
    content = f.read()

# Replace:
#         {/* Left Side: Breadcrumb Path & Page Title (Market Standard Pattern) */}
#         <div className="flex items-center gap-3 min-w-0">

# With:
#         {/* Left Side: Breadcrumb Path & Page Title (Market Standard Pattern) */}
#         <div className={`flex items-center gap-3 min-w-0 ${location.pathname === '/units' ? 'hidden md:invisible md:flex' : ''}`}>

left_side_pattern = r'\{/\* Left Side: Breadcrumb Path & Page Title \(Market Standard Pattern\) \*/\}\s*<div className="flex items-center gap-3 min-w-0">'
left_side_replacement = """{/* Left Side: Breadcrumb Path & Page Title (Market Standard Pattern) */}
        <div className={`flex items-center gap-3 min-w-0 ${location.pathname === '/units' ? 'invisible' : ''}`}>"""

content = re.sub(left_side_pattern, left_side_replacement, content)

with open("frontend/src/components/layout/Topbar.jsx", "w") as f:
    f.write(content)
print("Topbar updated.")
