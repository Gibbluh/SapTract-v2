import re

with open('frontend/src/components/layout/Sidebar.jsx', 'r') as f:
    content = f.read()

sidebar_old = r"""            \{\!isExpanded && \['remittances', 'maintenance'\]\.includes\(item\.key\) && notifications\.filter\(n => n\.type === item\.key && \!n\.readStatus\)\.length > 0 && \(\s+<span className="absolute right-1 top-1 w-2 h-2 rounded-full bg-red-500 border-2 border-\[\#1B3679\]"></span>\s+\)\}"""

sidebar_new = """            {!isExpanded && ['remittances', 'maintenance'].includes(item.key) && notifications.filter(n => n.type === item.key && !n.readStatus).length > 0 && (
              <span className="absolute -top-1 -right-1 flex h-4 w-4 items-center justify-center rounded-full bg-red-600 text-[9px] font-bold text-white border-2 border-[#1B3679] shadow-sm">
                {notifications.filter(n => n.type === item.key && !n.readStatus).length}
              </span>
            )}"""

content = re.sub(sidebar_old, sidebar_new, content, flags=re.DOTALL)

with open('frontend/src/components/layout/Sidebar.jsx', 'w') as f:
    f.write(content)
