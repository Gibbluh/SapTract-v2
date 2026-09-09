import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

sortable_item_regex = r"const SortableItem = \(\{ id, children, className \}\) => \{.*?\n\};"
new_sortable_item = """const SortableItem = ({ id, children, className }) => {
  const {
    attributes,
    listeners,
    setNodeRef,
    transform,
    transition,
    isDragging,
  } = useSortable({ id });

  const style = {
    transform: CSS.Transform.toString(transform),
    transition,
    opacity: isDragging ? 0 : 1, // Hide the original item so the gap is visible
  };

  return (
    <div ref={setNodeRef} style={style} className={`relative group ${className || ''}`} {...attributes} {...listeners}>
      {children}
    </div>
  );
};"""
content = re.sub(sortable_item_regex, new_sortable_item, content, flags=re.DOTALL)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
