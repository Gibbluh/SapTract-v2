import re

with open('frontend/src/components/layout/Sidebar.jsx', 'r') as f:
    content = f.read()

# Restore isHovered just so we don't break the code if we miss anything, 
# but actually let's completely remove it.
# First, let's fix the `<aside>` block
old_aside = r"""      <aside
        id="app-sidebar"
        className={`fixed top-0 left-0 h-screen \$\{currentThemeConfig.sidebar \|\| "bg-blue-950 text-blue-100 border-white/10"\} flex flex-col justify-between border-r z-40 transition-\[width,box-shadow\] duration-300 ease-in-out select-none \$\{
          isExpanded \? "w-64 shadow-2xl" : "w-20 shadow-md"
        \}`}
      >"""

new_aside = """      <aside
        id="app-sidebar"
        className={`fixed top-0 left-0 h-screen ${currentThemeConfig.sidebar || "bg-blue-950 text-blue-100 border-white/10"} flex flex-col justify-between border-r z-40 transition-[width,box-shadow,transform] duration-200 ease-out select-none group/sidebar ${
          isPinned ? "w-64 shadow-2xl" : "w-20 hover:w-64 shadow-md hover:shadow-2xl"
        }`}
      >"""

content = re.sub(old_aside, new_aside, content)

# Replace other `isExpanded` with group-hover logic.
# isExpanded ? "class1" : "class2" -> "class2 group-hover/sidebar:class1" (when not pinned)
# But if it is pinned, it should just be class1.
# So we can use: `${isPinned ? "class1" : "class2 group-hover/sidebar:class1"}`

# Let's write a targeted script to do this.
