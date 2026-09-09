import re

with open('frontend/src/components/layout/Sidebar.jsx', 'r') as f:
    content = f.read()

# 1. Fix gap/categorization missing teeth issue
content = content.replace('className={idx !== 0 ? "mt-4" : ""}', 'className={idx !== 0 ? (isExpanded ? "mt-4" : "mt-1") : ""}')

# 2. Fix the notification badge (make sure it's on top of the icon)
# My previous absolute fix was:
# <span className="absolute -top-1 -right-1 flex h-4 w-4 items-center justify-center rounded-full bg-red-600 text-[9px] font-bold text-white border-2 border-[#1B3679] shadow-sm">
# Wait, let's wrap the Icon in a relative div, if it isn't already relative.
# Actually, the icon container is: <div className="w-10 h-10 shrink-0 flex items-center justify-center">
# Let's make that relative.
content = content.replace('<div className="w-10 h-10 shrink-0 flex items-center justify-center">', '<div className="relative w-10 h-10 shrink-0 flex items-center justify-center">')

# Wait, if we made it relative, we can put the absolute badge INSIDE the icon container.
# Currently the absolute badge is at the end of the NavLink.
old_badge = r"""            \{\!isExpanded && \['remittances', 'maintenance'\]\.includes\(item\.key\) && notifications\.filter\(n => n\.type === item\.key && \!n\.readStatus\)\.length > 0 && \(\s+<span className="absolute -top-1 -right-1 flex h-4 w-4 items-center justify-center rounded-full bg-red-600 text-\[9px\] font-bold text-white border-2 border-\[\#1B3679\] shadow-sm">\s+\{notifications\.filter\(n => n\.type === item\.key && \!n\.readStatus\)\.length\}\s+</span>\s+\)\}"""

new_badge = """""" # We will remove it from the end of NavLink

content = re.sub(old_badge, new_badge, content, flags=re.DOTALL)

# And put it inside the icon container:
icon_container_code = r"""            <div className="relative w-10 h-10 shrink-0 flex items-center justify-center">
              <Icon
                size=\{20\}
                strokeWidth=\{isActive \? 2\.2 : 2\}
                className=\{`shrink-0 transition-colors duration-150 \$\{
                  isActive \? "text-white" : "text-white/70 group-hover:text-white"
                \}`\}
              />
            </div>"""

icon_container_new = """            <div className="relative w-10 h-10 shrink-0 flex items-center justify-center">
              <Icon
                size={20}
                strokeWidth={isActive ? 2.2 : 2}
                className={`shrink-0 transition-colors duration-150 ${
                  isActive ? "text-white" : "text-white/70 group-hover:text-white"
                }`}
              />
              {!isExpanded && ['remittances', 'maintenance'].includes(item.key) && notifications.filter(n => n.type === item.key && !n.readStatus).length > 0 && (
                <span className="absolute top-1 right-1 flex h-4 w-4 items-center justify-center rounded-full bg-red-600 text-[9px] font-bold text-white border-2 border-[#1B3679] shadow-sm z-10">
                  {notifications.filter(n => n.type === item.key && !n.readStatus).length}
                </span>
              )}
            </div>"""

content = re.sub(icon_container_code, icon_container_new, content, flags=re.DOTALL)

# 3. Remove the Logout button completely from the Sidebar
logout_btn_code = r"""          \{/\* Logout Button \*/\}.*?</button>"""
content = re.sub(logout_btn_code, "", content, flags=re.DOTALL)

with open('frontend/src/components/layout/Sidebar.jsx', 'w') as f:
    f.write(content)
