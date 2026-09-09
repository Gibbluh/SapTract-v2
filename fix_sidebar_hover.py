import re

with open('frontend/src/components/layout/Sidebar.jsx', 'r') as f:
    content = f.read()

# 1. Remove isHovered state
content = re.sub(r"  // Transient hover state when not permanently pinned\n  const \[isHovered, setIsHovered\] = useState\(false\);\n\n", "", content)

# 2. Update isExpanded to only track isPinned
content = content.replace("const isExpanded = isPinned || isHovered;", "const isExpanded = isPinned;")

# 3. Add a group class to the aside and replace React hover events with CSS group-hover
# First, remove onMouseEnter and onMouseLeave
content = re.sub(r"\s*onMouseEnter=\{.*?\}\s*onMouseLeave=\{.*?\}\s*", "\n        ", content)

# Modify the aside classes to use group and handle the hover state with CSS
old_aside = r"""      <aside
        id="app-sidebar"
        className={`fixed top-0 left-0 h-screen \$\{currentThemeConfig\.sidebar \|\| "bg-blue-950 text-blue-100 border-white/10"\} flex flex-col justify-between border-r z-40 transition-\[width,box-shadow\] duration-300 ease-in-out select-none \$\{
          isExpanded \? "w-64 shadow-2xl" : "w-20 shadow-md"
        \}`}
      >"""

new_aside = """      <aside
        id="app-sidebar"
        className={`fixed top-0 left-0 h-screen ${currentThemeConfig.sidebar || "bg-blue-950 text-blue-100 border-white/10"} flex flex-col justify-between border-r z-40 transition-[width,box-shadow] duration-200 ease-out select-none group/sidebar ${
          isPinned ? "w-64 shadow-2xl" : "w-20 shadow-md hover:w-64 hover:shadow-2xl"
        }`}
      >"""
content = re.sub(old_aside, new_aside, content)


# Now, we need to replace all `isExpanded ? "classA" : "classB"` with CSS group-hover logic inside the sidebar.
# Wait, this might be too complex for a simple regex if there are many places.
# Let's see how many places use isExpanded for styling inside the aside.
