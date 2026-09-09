import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# 1. Add DragOverlay to imports
content = content.replace("  useSensors,\n} from '@dnd-kit/core';", "  useSensors,\n  DragOverlay,\n} from '@dnd-kit/core';")

# 2. Update SortableItem to return a placeholder when dragging
sortable_item_regex = r"const SortableItem = \(\{ id, children, className \}\) => \{.*?\n\s+return \(\n\s+<div ref=\{setNodeRef\}[^\n]+\n\s+\{children\}\n\s+</div>\n\s+\);\n\};"
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
    transform: CSS.Translate.toString(transform),
    transition,
  };

  if (isDragging) {
    return (
      <div 
        ref={setNodeRef} 
        style={style} 
        className={`border-2 border-dashed border-blue-400 dark:border-blue-500 bg-blue-50/50 dark:bg-blue-900/20 rounded-3xl opacity-50 ${className || ''}`}
      />
    );
  }

  return (
    <div ref={setNodeRef} style={style} className={`relative group ${className || ''}`} {...attributes} {...listeners}>
      {children}
    </div>
  );
};"""
content = re.sub(sortable_item_regex, new_sortable_item, content, flags=re.DOTALL)

# 3. Rename `widgets` to `widgetContents`, and remove SortableItem wrappers
content = content.replace("const widgets = {", "const widgetContents = {")
content = re.sub(r"<SortableItem id=\"([^\"]+)\" key=\"([^\"]+)\" className=\{WIDGET_CLASSES\['[^']+'\]\}>\n", "", content)
content = re.sub(r"</SortableItem>", "", content)

# 4. Add activeId state and onDragStart
content = content.replace("const [widgetOrder, setWidgetOrder] = useState([", "const [activeId, setActiveId] = useState(null);\n  const [widgetOrder, setWidgetOrder] = useState([")

# 5. Add handleDragStart
content = content.replace("const handleDragEnd = (event) => {", "const handleDragStart = (event) => {\n    setActiveId(event.active.id);\n  };\n\n  const handleDragEnd = (event) => {\n    setActiveId(null);")

# 6. Update rendering
old_render = r"<SortableContext items=\{widgetOrder\} strategy=\{rectSortingStrategy\}>\n\s+<div className=\"grid grid-cols-12 gap-5 grid-flow-row-dense\">\n\s+\{widgetOrder\.map\(id => widgets\[id\]\)\}\n\s+</div>\n\s+</SortableContext>"
new_render = """<SortableContext items={widgetOrder} strategy={rectSortingStrategy}>
          <div className="grid grid-cols-12 gap-5 grid-flow-row-dense">
            {widgetOrder.map(id => (
              <SortableItem key={id} id={id} className={WIDGET_CLASSES[id]}>
                {widgetContents[id]}
              </SortableItem>
            ))}
          </div>
        </SortableContext>
        
        <DragOverlay>
          {activeId ? (
            <div className={`shadow-2xl opacity-90 scale-105 cursor-grabbing ${WIDGET_CLASSES[activeId]}`}>
              {widgetContents[activeId]}
            </div>
          ) : null}
        </DragOverlay>"""
content = re.sub(old_render, new_render, content)

# 7. Add onDragStart to DndContext
content = content.replace("<DndContext sensors={sensors} collisionDetection={closestCenter} onDragEnd={handleDragEnd}>", "<DndContext sensors={sensors} collisionDetection={closestCenter} onDragStart={handleDragStart} onDragEnd={handleDragEnd}>")


with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)

print("Done")
