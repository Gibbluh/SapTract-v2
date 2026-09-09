import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# I need to find the entire state initialization and replace it.
# state_init = "const [metricsOrder, setMetricsOrder]" to "const handleDragEnd = (event) => { ... };"
# I will replace it with unified state

unified_state = """  const [widgetOrder, setWidgetOrder] = useState([
    'metric-revenue', 'metric-active', 'metric-pending', 'metric-users', 'metric-alerts',
    'chart-revenue', 'chart-fleet', 'chart-dispatches'
  ]);

  const sensors = useSensors(
    useSensor(PointerSensor, { activationConstraint: { distance: 5 } }),
    useSensor(KeyboardSensor, { coordinateGetter: sortableKeyboardCoordinates })
  );

  const handleDragEnd = (event) => {
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

content = re.sub(r'const \[metricsOrder.*?handleDragEnd = \(event\) => \{.*?\n  \};\n', unified_state + '\n', content, flags=re.DOTALL)

# Now rewrite the components dictionaries into one
# I'll just find "const metricsComponents = {" and "const chartsComponents = {" and merge them.
# I'll extract them completely.
# This requires some care. Let's write a targeted script to extract the body of SuperAdminDashboard and completely redefine the widgets map and the return statement.
