import re

with open('frontend/src/components/layout/Sidebar.jsx', 'r') as f:
    content = f.read()

# Restore logout button instead of user profile on bottom of Sidebar
profile_regex = r"          \{/\* User Profile / Logout Button \*/\}.*?          </button>"
logout_code = """          {/* Logout Button */}
          <button
            id="sidebar-logout-btn"
            type="button"
            onClick={() => setShowLogout(true)}
            title="Logout"
            className="group flex items-center h-11 w-full px-2 rounded-xl text-white/70 hover:bg-white/5 hover:text-red-400 transition-all duration-150"
          >
            <div className="w-10 h-10 shrink-0 flex items-center justify-center">
              <LogOut size={18} strokeWidth={2} className="shrink-0 group-hover:text-red-400 transition-colors" />
            </div>
            <span
              className={`ml-2 text-sm font-medium whitespace-nowrap overflow-hidden transition-all duration-300 ease-in-out ${
                isExpanded
                  ? "opacity-100 max-w-[170px] translate-x-0"
                  : "opacity-0 max-w-0 -translate-x-4 pointer-events-none"
              }`}
            >
              Logout
            </span>
          </button>"""

content = re.sub(profile_regex, logout_code, content, flags=re.DOTALL)

with open('frontend/src/components/layout/Sidebar.jsx', 'w') as f:
    f.write(content)
