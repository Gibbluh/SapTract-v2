import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

drag_over_func = """
  const handleDragOver = (event) => {
    const { active, over } = event;
    if (!over) return;
    if (active.id !== over.id) {
      setWidgetOrder((items) => {
        const oldIndex = items.indexOf(active.id);
        const newIndex = items.indexOf(over.id);
        return arrayMove(items, oldIndex, newIndex);
      });
    }
  };
"""

content = content.replace("  const handleDragEnd = (event) => {", drag_over_func + "\n  const handleDragEnd = (event) => {")

dnd_context = "<DndContext sensors={sensors} collisionDetection={closestCenter} onDragStart={handleDragStart} onDragEnd={handleDragEnd}>"
dnd_context_new = "<DndContext sensors={sensors} collisionDetection={closestCenter} onDragStart={handleDragStart} onDragOver={handleDragOver} onDragEnd={handleDragEnd}>"
content = content.replace(dnd_context, dnd_context_new)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
