import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# Since we move the state update to onDragOver, we don't need it in onDragEnd.
# However, it's safer to keep the final state check in onDragEnd too, but we can simplify it.
# Actually, since it's already there, it won't do anything because active.id will be equal to over.id
# if they were already swapped. But let's leave it as is, just clear activeId.

content = content.replace("  const handleDragEnd = (event) => {\n    setActiveId(null);\n    const { active, over } = event;\n    if (!over) return;\n    if (active.id !== over.id) {\n      setWidgetOrder((items) => {\n        const oldIndex = items.indexOf(active.id);\n        const newIndex = items.indexOf(over.id);\n        return arrayMove(items, oldIndex, newIndex);\n      });\n    }\n  };", "  const handleDragEnd = (event) => {\n    setActiveId(null);\n  };")


with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
