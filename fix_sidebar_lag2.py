import re

with open('frontend/src/components/layout/Sidebar.jsx', 'r') as f:
    content = f.read()

# Fix the structural layout spacer to only expand when PINNED, not when hovered.
# This prevents the whole page from reflowing and lagging on hover.
old_spacer = r"""      \{/\* Structural layout spacer that reserves space in the document flow - expands with sidebar \*/\}
      <div
        className={`shrink-0 transition-\[width\] duration-150 ease-out relative \$\{
          isExpanded \? "w-64" : "w-20"
        \}`}
      />"""

new_spacer = """      {/* Structural layout spacer that reserves space in the document flow - only expands when pinned to avoid layout thrashing on hover */}
      <div
        className={`shrink-0 transition-[width] duration-300 ease-in-out relative ${
          isPinned ? "w-64" : "w-20"
        }`}
      />"""

content = re.sub(old_spacer, new_spacer, content)

# I should also revert the transition durations for the rest of the sidebar to duration-300 ease-in-out
# because now that layout thrashing is gone, it will be smooth anyway.
content = content.replace('transition-[width,box-shadow] duration-150 ease-out', 'transition-[width,box-shadow] duration-300 ease-in-out')
content = content.replace('transition-[width] duration-150 ease-out', 'transition-[width] duration-300 ease-in-out')
content = content.replace('transition-all duration-150 ease-out', 'transition-all duration-300 ease-in-out')

with open('frontend/src/components/layout/Sidebar.jsx', 'w') as f:
    f.write(content)
