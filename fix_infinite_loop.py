import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# 1. Remove onDragOver from DndContext
content = content.replace(" onDragOver={handleDragOver}", "")

# 2. Remove handleDragOver function and restore handleDragEnd
drag_funcs_regex = r"  const handleDragOver = \(event\) => \{.*?\n  \};\n\n  const handleDragEnd = \(event\) => \{\n    setActiveId\(null\);\n  \};"
new_drag_funcs = """  const handleDragEnd = (event) => {
    setActiveId(null);
    const { active, over } = event;
    if (!over) return;
    if (active.id !== over.id) {
      setWidgetOrder((items) => {
        const oldIndex = items.indexOf(active.id);
        const newIndex = items.indexOf(over.id);
        return arrayMove(items, oldIndex, newIndex);
      });
    }
  };"""
content = re.sub(drag_funcs_regex, new_drag_funcs, content, flags=re.DOTALL)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
