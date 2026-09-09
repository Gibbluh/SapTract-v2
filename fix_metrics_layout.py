import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# 1. Update WIDGET_CLASSES for metrics
old_classes = """  'metric-revenue': 'col-span-12 sm:col-span-4 h-full flex',
  'metric-fuel': 'col-span-12 sm:col-span-4 h-full flex',
  'metric-users': 'col-span-12 sm:col-span-4 h-full flex',"""
new_classes = """  'metric-revenue': 'col-span-12 sm:col-span-6 h-full flex',
  'metric-fuel': 'col-span-12 sm:col-span-6 h-full flex',"""
content = content.replace(old_classes, new_classes)

# 2. Update widgetOrder
old_order = """  const [widgetOrder, setWidgetOrder] = useState([
    'metric-revenue', 'metric-fuel', 'metric-users',
    'chart-revenue', 'chart-fleet', 'chart-dispatches'
  ]);"""
new_order = """  const [widgetOrder, setWidgetOrder] = useState([
    'metric-revenue', 'metric-fuel',
    'chart-revenue', 'chart-fleet', 'chart-dispatches'
  ]);"""
content = content.replace(old_order, new_order)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
