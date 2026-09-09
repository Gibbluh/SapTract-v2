import re

with open('frontend/src/components/layout/Sidebar.jsx', 'r') as f:
    content = f.read()

# Change the spacer to expand on hover (isExpanded) instead of just when pinned
content = content.replace(
    'isPinned ? "w-64" : "w-20"',
    'isExpanded ? "w-64" : "w-20"'
)

# Wait, let's make sure there's only one occurrence or all occurrences are correct
# Actually, the switch in the bottom controls also uses `isPinned ? "w-64" : "w-20"`? No, it uses other classes.
# Let's be precise.

with open('frontend/src/components/layout/Sidebar.jsx', 'w') as f:
    f.write(content)
