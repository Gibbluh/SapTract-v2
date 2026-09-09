import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# --- 1. Modify WIDGET_CLASSES ---
old_widget_classes = """const WIDGET_CLASSES = {
  'metric-revenue': 'col-span-12 sm:col-span-6 xl:col-span-3 2xl:col-span-2 h-full flex',
  'metric-active': 'col-span-12 sm:col-span-6 xl:col-span-3 2xl:col-span-2 h-full flex',
  'metric-pending': 'col-span-12 sm:col-span-6 xl:col-span-2 h-full flex',
  'metric-users': 'col-span-12 sm:col-span-6 xl:col-span-2 h-full flex',
  'metric-alerts': 'col-span-12 sm:col-span-6 xl:col-span-2 h-full flex',
  'chart-revenue': 'col-span-12 lg:col-span-8 flex h-full',
  'chart-fleet': 'col-span-12 lg:col-span-4 flex h-full',
  'chart-dispatches': 'col-span-12 lg:col-span-4 flex h-full'
};"""
new_widget_classes = """const WIDGET_CLASSES = {
  'metric-revenue': 'col-span-12 sm:col-span-4 h-full flex',
  'metric-fuel': 'col-span-12 sm:col-span-4 h-full flex',
  'metric-users': 'col-span-12 sm:col-span-4 h-full flex',
  'chart-revenue': 'col-span-12 lg:col-span-8 flex h-full',
  'chart-fleet': 'col-span-12 lg:col-span-4 flex h-full',
  'chart-dispatches': 'col-span-12 lg:col-span-12 flex h-full' // Changed to full width to fit leaderboard nicely
};"""
content = content.replace(old_widget_classes, new_widget_classes)

# --- 2. State & Hooks ---
old_state = """  const [timeFilter, setTimeFilter] = useState('Today');
  const [activeId, setActiveId] = useState(null);
  const [widgetOrder, setWidgetOrder] = useState([
    'metric-revenue', 'metric-active', 'metric-pending', 'metric-users', 'metric-alerts',
    'chart-revenue', 'chart-fleet', 'chart-dispatches'
  ]);"""
new_state = """  const [timeFilter, setTimeFilter] = useState('Today');
  const [activeId, setActiveId] = useState(null);
  const [revenueTab, setRevenueTab] = useState('Today');
  const [driverTab, setDriverTab] = useState('Drivers');
  const [widgetOrder, setWidgetOrder] = useState([
    'metric-revenue', 'metric-fuel', 'metric-users',
    'chart-revenue', 'chart-fleet', 'chart-dispatches'
  ]);"""
content = content.replace(old_state, new_state)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
