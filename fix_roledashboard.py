with open('frontend/src/pages/RoleDashboard.jsx', 'r') as f:
    content = f.read()

old_str = """        <div className="mb-6">
          <h1 className="text-3xl font-black text-slate-900 tracking-tight">
            Welcome back, {welcomeLabel}
          </h1>
          <p className="text-sm font-medium text-slate-500 mt-1">
            Here's what's happening today.
          </p>
        </div>"""

new_str = ""

new_content = content.replace(old_str, new_str)

# Also update the background of the layout to support dark mode in RoleDashboard
new_content = new_content.replace('className="min-h-screen bg-slate-50 text-black"', 'className="min-h-screen dark:bg-slate-950 bg-slate-50 dark:text-white text-black"')

with open('frontend/src/pages/RoleDashboard.jsx', 'w') as f:
    f.write(new_content)

