import re

with open('frontend/src/components/layout/Sidebar.jsx', 'r') as f:
    content = f.read()

# 1. Update CATEGORIES names and wrap Nav items in a reusable function
nav_item_renderer = """
  const renderNavItem = (item) => {
    const Icon = getIcon(item.key);
    return (
      <NavLink
        key={item.key}
        to={item.path}
        className={({ isActive }) =>
          `group flex items-center h-11 w-full px-2 rounded-xl transition-all duration-150 border-l-4 ${
            isActive
              ? "bg-white/10 text-white font-semibold border-red-600 shadow-sm"
              : "border-transparent text-white/70 hover:bg-white/5 hover:text-white"
          }`
        }
      >
        {({ isActive }) => (
          <>
            <div className="w-10 h-10 shrink-0 flex items-center justify-center">
              <Icon
                size={20}
                strokeWidth={isActive ? 2.2 : 2}
                className={`shrink-0 transition-colors duration-150 ${
                  isActive ? "text-white" : "text-white/70 group-hover:text-white"
                }`}
              />
            </div>
            <span
              className={`ml-2 text-sm font-medium whitespace-nowrap overflow-hidden transition-all duration-300 ease-in-out ${
                isExpanded
                  ? "opacity-100 max-w-[170px] translate-x-0"
                  : "opacity-0 max-w-0 -translate-x-4 pointer-events-none"
              }`}
            >
              {item.label}
            </span>
            {item.key === 'remittances' && notifications.filter(n => n.type === 'remittances' && !n.readStatus).length > 0 && (
              <span className={`ml-auto bg-red-600 text-white text-[10px] font-bold px-1.5 py-0.5 rounded-full transition-opacity duration-300 ${isExpanded ? 'opacity-100' : 'opacity-0 hidden'}`}>
                {notifications.filter(n => n.type === 'remittances' && !n.readStatus).length}
              </span>
            )}
            {item.key === 'maintenance' && notifications.filter(n => n.type === 'maintenance' && !n.readStatus).length > 0 && (
              <span className={`ml-auto bg-red-600 text-white text-[10px] font-bold px-1.5 py-0.5 rounded-full transition-opacity duration-300 ${isExpanded ? 'opacity-100' : 'opacity-0 hidden'}`}>
                {notifications.filter(n => n.type === 'maintenance' && !n.readStatus).length}
              </span>
            )}
            {!isExpanded && ['remittances', 'maintenance'].includes(item.key) && notifications.filter(n => n.type === item.key && !n.readStatus).length > 0 && (
              <span className="absolute right-1 top-1 w-2 h-2 rounded-full bg-red-500 border-2 border-[#1B3679]"></span>
            )}
          </>
        )}
      </NavLink>
    );
  };
"""

# Find the start of the `<nav>` to replace everything inside
start_idx = content.find('<nav className="px-2.5 flex-1')
end_idx = content.find('</nav>', start_idx) + 6

nav_replacement = """          <nav className="px-2.5 flex-1 min-h-0 overflow-y-auto overflow-x-hidden py-3 space-y-1">
            {isSuperAdmin ? (
              CATEGORIES.map((category, idx) => {
                const categoryItems = items.filter(item => category.keys.includes(item.key));
                if (categoryItems.length === 0) return null;

                return (
                  <div key={category.name} className={idx !== 0 ? "mt-4" : ""}>
                    {/* Category Header - Horizontal Slide */}
                    <div className={`px-3 pb-1 text-[10px] font-bold text-white/40 tracking-wider transition-all duration-300 ease-in-out overflow-hidden whitespace-nowrap ${
                      isExpanded
                        ? "opacity-100 max-w-[170px] translate-x-0"
                        : "opacity-0 max-w-0 -translate-x-4 pointer-events-none"
                    }`}>
                      {category.name}
                    </div>
                    
                    <div className="space-y-1">
                      {categoryItems.map((item) => renderNavItem(item))}
                    </div>
                  </div>
                );
              })
            ) : (
              <div className="space-y-1">
                {items.map(item => renderNavItem(item))}
              </div>
            )}
            
            {items.length === 0 && (
              <div
                className={`px-3 py-3 text-sm font-medium text-white/70 overflow-hidden whitespace-nowrap transition-all duration-300 ${
                  isExpanded ? "opacity-100" : "opacity-0"
                }`}
              >
                Menu unavailable for this account.
              </div>
            )}
          </nav>"""

new_content = content[:start_idx] + nav_replacement + content[end_idx:]
new_content = new_content.replace('const isExpanded = isPinned || isHovered;', 'const isExpanded = isPinned || isHovered;\n' + nav_item_renderer)

# 2. Update category names to remove jargon
new_content = new_content.replace('"CORE OPERATIONS"', '"Operations"')
new_content = new_content.replace('"TERMINAL & FINANCE"', '"Finance"')
new_content = new_content.replace('"FLEET MAINTENANCE"', '"Maintenance"')
new_content = new_content.replace('"INTELLIGENCE & PUBLIC"', '"System"')

with open('frontend/src/components/layout/Sidebar.jsx', 'w') as f:
    f.write(new_content)
