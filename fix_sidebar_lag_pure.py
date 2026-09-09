import re

with open('frontend/src/components/layout/Sidebar.jsx', 'r') as f:
    content = f.read()

# 1. We remove isHovered state completely. We only track isPinned.
content = re.sub(r"  // Transient hover state when not permanently pinned\n  const \[isHovered, setIsHovered\] = useState\(false\);\n", "", content)

content = content.replace("const isExpanded = isPinned || isHovered;", "const isExpanded = isPinned;")

content = re.sub(r"\s*onMouseEnter=\{.*?\}\s*", "\n        ", content)
content = re.sub(r"\s*onMouseLeave=\{.*?\}\s*", "\n        ", content)

# 2. Add group/sidebar to aside and use group-hover/sidebar
# Wait, let's just do a manual replace of `isExpanded ? "class1" : "class2"` with CSS group hover!
# Actually, an easier way to get pure CSS hover is to keep isHovered, but remove the transition classes on the spacer.
# Wait, I already removed transition on the spacer in the previous step?
# Let's see how spacer is currently defined.
