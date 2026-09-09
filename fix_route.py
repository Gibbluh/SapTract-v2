import re

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

# Fix route filter button to also have the count
target = """<Filter className="w-4 h-4 text-gray-400" />
              Route: {routeFilter}
              <ChevronDown className="w-4 h-4 text-gray-400 ml-1" />"""
replacement = """<Filter className="w-4 h-4 text-gray-400" />
              Route: {routeFilter}
              <span className="bg-gray-100 text-gray-600 px-1.5 py-0.5 rounded-full text-[10px] font-bold ml-1">
                {routeFilter === 'All' ? unitsList.length : 
                 routeFilter === 'Unassigned' ? unitsList.filter(u => u.route === 'UNASSIGNED').length :
                 unitsList.filter(u => u.route.toLowerCase() === routeFilter.toLowerCase()).length}
              </span>
              <ChevronDown className="w-4 h-4 text-gray-400" />"""
                          
content = content.replace(target, replacement)

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "w") as f:
    f.write(content)
