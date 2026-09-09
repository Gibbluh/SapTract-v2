import re

with open('frontend/src/components/layout/Topbar.jsx', 'r') as f:
    content = f.read()

# Add the user profile dropdown back to the Topbar right side
# Find the NotificationBell block to insert after it
bell_regex = r"(<NotificationBell userId=\{user\?._id \|\| user\?\.id\} />\s*</div>)"

profile_code = """
          <div className="h-6 w-px bg-current opacity-20 hidden sm:block" />
          {/* User Account Pill Dropdown */}
          <div className="relative">
            <button
              id="topbar-user-profile-menu-trigger"
              type="button"
              onClick={() => setProfileOpen((prev) => !prev)}
              className="flex items-center gap-2 p-1 pl-1.5 sm:pr-2.5 rounded-xl border border-current/20 hover:bg-white/10 transition-all focus:outline-none focus:ring-2 focus:ring-blue-500/20"
            >
              <div className="w-8 h-8 rounded-lg bg-blue-900 text-white flex items-center justify-center font-bold text-xs shadow-xs shrink-0">
                SA
              </div>
              <div className="hidden sm:flex flex-col text-left leading-tight pr-1">
                <span className="text-xs font-bold truncate max-w-[120px]">
                  {user?.fullName || "Super Administrator"}
                </span>
                <span
                  className="text-[9px] font-semibold px-1 py-[1px] rounded border mt-0.5 inline-block w-fit bg-red-100 text-red-700 border-red-200 dark:bg-red-900/30 dark:text-red-400 dark:border-red-800"
                >
                  Super Admin
                </span>
              </div>
              <ChevronDown
                size={14}
                className={`opacity-70 transition-transform duration-200 ${
                  profileOpen ? "rotate-180" : ""
                }`}
              />
            </button>
            {/* Profile Dropdown Menu */}
            {profileOpen && (
              <>
                <div
                  className="fixed inset-0 z-40"
                  onClick={() => setProfileOpen(false)}
                />
                <div
                  id="topbar-profile-dropdown-menu"
                  className="absolute right-0 mt-2 w-60 bg-white rounded-2xl border border-slate-200 shadow-xl py-2 z-50 animate-in fade-in zoom-in-95 duration-150"
                >
                  <div className="px-4 py-2.5 border-b border-slate-100">
                    <p className="text-xs font-bold text-slate-900 truncate">
                      {user?.fullName || "Super Administrator"}
                    </p>
                    <p className="text-[11px] text-slate-500 truncate">
                      admin@saptrac.com
                    </p>
                    <div className="mt-2 flex items-center gap-1.5">
                      <span
                        className="text-[10px] font-semibold px-2 py-0.5 rounded border inline-block bg-red-100 text-red-700 border-red-200"
                      >
                        Super Admin
                      </span>
                      <span className="text-[10px] text-slate-400">ID: ADMIN-01</span>
                    </div>
                  </div>
                  <div className="py-1">
                    <button
                      type="button"
                      onClick={() => {
                        setProfileOpen(false);
                        navigate("/dashboard");
                      }}
                      className="w-full px-4 py-2 text-xs font-medium text-slate-700 hover:bg-slate-50 flex items-center gap-2.5 transition-colors text-left"
                    >
                      <ShieldCheck size={15} className="text-slate-400" />
                      Fleet Dashboard
                    </button>
                    <div className="h-px bg-slate-100 my-1" />
                    <button
                      type="button"
                      onClick={() => {
                        setProfileOpen(false);
                        logout();
                        navigate("/");
                      }}
                      className="w-full px-4 py-2 text-xs font-medium text-red-600 hover:bg-red-50 flex items-center gap-2.5 transition-colors text-left"
                    >
                      <LogOut size={15} className="text-red-500" />
                      Logout
                    </button>
                  </div>
                </div>
              </>
            )}
          </div>"""

# Replace in content
content = re.sub(bell_regex, r"\1" + profile_code, content)

with open('frontend/src/components/layout/Topbar.jsx', 'w') as f:
    f.write(content)
