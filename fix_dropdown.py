import re

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

# Replace the dynamic bg color with an inline map
target = """<div className={`w-2 h-2 rounded-full bg-${route.color}-500`}></div>"""
replacement = """<div className={`w-2 h-2 rounded-full ${
                            route.color === 'blue' ? 'bg-blue-500' : 
                            route.color === 'emerald' ? 'bg-emerald-500' :
                            route.color === 'purple' ? 'bg-purple-500' :
                            route.color === 'orange' ? 'bg-orange-500' :
                            route.color === 'red' ? 'bg-red-500' : 'bg-gray-500'
                          }`}></div>"""
                          
content = content.replace(target, replacement)

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "w") as f:
    f.write(content)

