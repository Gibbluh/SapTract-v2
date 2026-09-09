import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# Add imports
imports = """import React, { useState } from "react";
import {
  DndContext,
  closestCenter,
  KeyboardSensor,
  PointerSensor,
  useSensor,
  useSensors,
} from '@dnd-kit/core';
import {
  arrayMove,
  SortableContext,
  sortableKeyboardCoordinates,
  rectSortingStrategy,
  horizontalListSortingStrategy
} from '@dnd-kit/sortable';
import { useSortable } from '@dnd-kit/sortable';
import { CSS } from '@dnd-kit/utilities';
import { GripHorizontal } from "lucide-react";"""

content = content.replace('import React from "react";', imports)

# We need a SortableItem component
sortable_item = """
const SortableItem = ({ id, children, className }) => {
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
    zIndex: isDragging ? 50 : 1,
    opacity: isDragging ? 0.8 : 1,
  };

  return (
    <div ref={setNodeRef} style={style} className={`relative group ${className || ''}`}>
      <div 
        {...attributes} 
        {...listeners}
        className="absolute top-2 right-2 w-6 h-6 bg-white/80 backdrop-blur-sm rounded-md flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity cursor-grab active:cursor-grabbing shadow-sm border border-slate-200 z-10"
      >
        <GripHorizontal className="w-3.5 h-3.5 text-slate-500" />
      </div>
      {children}
    </div>
  );
};
"""
content = content.replace('const SuperAdminDashboard =', sortable_item + '\nconst SuperAdminDashboard =')

# Now inside SuperAdminDashboard
# We need state for order.
state_init = """  const [metricsOrder, setMetricsOrder] = useState(['metric-revenue', 'metric-active', 'metric-pending', 'metric-users', 'metric-alerts']);
  const [chartsOrder, setChartsOrder] = useState(['chart-revenue', 'chart-fleet']);

  const sensors = useSensors(
    useSensor(PointerSensor, { activationConstraint: { distance: 5 } }),
    useSensor(KeyboardSensor, { coordinateGetter: sortableKeyboardCoordinates })
  );

  const handleDragEnd = (event) => {
    const { active, over } = event;
    if (!over) return;

    if (active.id !== over.id) {
      if (metricsOrder.includes(active.id)) {
        setMetricsOrder((items) => {
          const oldIndex = items.indexOf(active.id);
          const newIndex = items.indexOf(over.id);
          return arrayMove(items, oldIndex, newIndex);
        });
      } else if (chartsOrder.includes(active.id)) {
        setChartsOrder((items) => {
          const oldIndex = items.indexOf(active.id);
          const newIndex = items.indexOf(over.id);
          return arrayMove(items, oldIndex, newIndex);
        });
      }
    }
  };"""

content = re.sub(r'const SuperAdminDashboard = \(\{ dashboard, fleetHealth, formatCurrency, formatNumber \}\) => \{', 
                 'const SuperAdminDashboard = ({ dashboard, fleetHealth, formatCurrency, formatNumber }) => {\n' + state_init, 
                 content)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
