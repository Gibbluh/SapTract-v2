import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# Update WIDGET_CLASSES
old_classes = r"""const WIDGET_CLASSES = \{
  'chart-revenue': 'col-span-12 lg:col-span-6 flex h-full',
  'chart-dispatches': 'col-span-12 lg:col-span-4 flex h-full',
  'metric-revenue': 'col-span-12 sm:col-span-6 lg:col-span-4 flex h-full',
  'metric-fuel': 'col-span-12 sm:col-span-6 lg:col-span-4 flex h-full',
  'chart-fleet': 'col-span-12 lg:col-span-4 flex h-full',
  'chart-weekly-earnings': 'col-span-12 lg:col-span-6 flex h-full min-h-\[350px\]',
\};"""

new_classes = """const WIDGET_CLASSES = {
  'chart-revenue': 'col-span-12 lg:col-span-4 lg:row-span-2 flex h-full min-h-[350px]',
  'chart-weekly-earnings': 'col-span-12 lg:col-span-4 lg:row-span-2 flex h-full min-h-[350px]',
  'chart-dispatches': 'col-span-12 lg:col-span-4 flex h-full',
  'chart-fleet': 'col-span-12 lg:col-span-4 flex h-full',
  'metric-revenue': 'col-span-12 lg:col-span-6 flex h-full',
  'metric-fuel': 'col-span-12 lg:col-span-6 flex h-full',
};"""
content = re.sub(old_classes, new_classes, content)

# Update widgetOrder
old_order = r"""  const \[widgetOrder, setWidgetOrder\] = useState\(\[
    'chart-revenue', 'chart-weekly-earnings', 'chart-dispatches', 'metric-revenue', 'metric-fuel', 'chart-fleet'
  \]\);"""

new_order = """  const [widgetOrder, setWidgetOrder] = useState([
    'chart-revenue', 'chart-weekly-earnings', 'chart-dispatches', 'chart-fleet', 'metric-revenue', 'metric-fuel'
  ]);"""
content = re.sub(old_order, new_order, content)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)

