import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

old_classes = r"""const WIDGET_CLASSES = \{
  'chart-revenue': 'col-span-12 lg:col-span-4 lg:row-span-2 flex h-full min-h-\[350px\]',
  'chart-weekly-earnings': 'col-span-12 lg:col-span-4 lg:row-span-2 flex h-full min-h-\[350px\]',
  'chart-dispatches': 'col-span-12 lg:col-span-4 flex h-full',
  'chart-fleet': 'col-span-12 lg:col-span-4 flex h-full',
  'metric-revenue': 'col-span-12 lg:col-span-6 flex h-full',
  'metric-fuel': 'col-span-12 lg:col-span-6 flex h-full',
\};"""

new_classes = """const WIDGET_CLASSES = {
  'chart-revenue': 'col-span-12 lg:col-span-6 flex h-full min-h-[350px]',
  'chart-weekly-earnings': 'col-span-12 lg:col-span-6 flex h-full min-h-[350px]',
  'chart-dispatches': 'col-span-12 lg:col-span-6 flex h-full',
  'chart-fleet': 'col-span-12 lg:col-span-6 flex h-full',
  'metric-revenue': 'col-span-12 lg:col-span-6 flex h-full',
  'metric-fuel': 'col-span-12 lg:col-span-6 flex h-full',
};"""

content = re.sub(old_classes, new_classes, content)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)

