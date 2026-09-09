import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# Fix Revenue Overview height
# Change WIDGET_CLASSES to use flex layout
old_classes = r"""const WIDGET_CLASSES = \{
  'chart-revenue': 'col-span-12 lg:col-span-8 lg:row-span-2 flex h-full min-h-\[400px\]',
  'chart-dispatches': 'col-span-12 lg:col-span-4 flex h-full',
  'chart-fleet': 'col-span-12 lg:col-span-4 flex h-full',
  'metric-revenue': 'col-span-12 sm:col-span-6 lg:col-span-4 flex h-full',
  'metric-fuel': 'col-span-12 sm:col-span-6 lg:col-span-4 flex h-full',
\};"""

new_classes = """const WIDGET_CLASSES = {
  'chart-revenue': 'col-span-12 lg:col-span-8 flex h-full',
  'chart-dispatches': 'col-span-12 lg:col-span-4 flex h-full',
  'metric-revenue': 'col-span-12 sm:col-span-6 lg:col-span-4 flex h-full',
  'metric-fuel': 'col-span-12 sm:col-span-6 lg:col-span-4 flex h-full',
  'chart-fleet': 'col-span-12 lg:col-span-4 flex h-full',
};"""
content = re.sub(old_classes, new_classes, content)

# Change grid layout to normal (no row-dense)
content = content.replace('<div className="grid grid-cols-1 md:grid-cols-12 gap-4 lg:gap-6 pb-20 grid-flow-row-dense">', '<div className="grid grid-cols-1 lg:grid-cols-12 gap-4 lg:gap-6 pb-20">')

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
