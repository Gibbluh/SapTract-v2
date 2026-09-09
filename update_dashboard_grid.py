import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# 1. Update the parent grid
content = content.replace(
    'className="grid grid-cols-12 gap-5 grid-flow-row-dense"',
    'className="grid grid-cols-1 sm:grid-cols-10 gap-5 grid-flow-row-dense"'
)

# 2. Update WIDGET_CLASSES
old_classes = r"""const WIDGET_CLASSES = \{
  'chart-revenue': 'col-span-12 lg:col-span-6 flex h-full min-h-\[350px\]',
  'chart-weekly-earnings': 'col-span-12 lg:col-span-6 flex h-full min-h-\[350px\]',
  'chart-dispatches': 'col-span-12 lg:col-span-6 flex h-full',
  'chart-fleet': 'col-span-12 lg:col-span-6 flex h-full',
  'metric-revenue': 'col-span-12 lg:col-span-6 flex h-full',
  'metric-fuel': 'col-span-12 lg:col-span-6 flex h-full',
\};"""

new_classes = """const WIDGET_CLASSES = {
  'chart-revenue': 'sm:col-span-10 lg:col-span-4 lg:row-span-2 flex h-full min-h-[400px]',
  'chart-weekly-earnings': 'sm:col-span-10 lg:col-span-4 lg:row-span-2 flex h-full min-h-[400px]',
  'chart-dispatches': 'sm:col-span-5 lg:col-span-2 flex h-full',
  'chart-fleet': 'sm:col-span-5 lg:col-span-2 flex h-full',
  'metric-revenue': 'sm:col-span-5 lg:col-span-5 flex h-full',
  'metric-fuel': 'sm:col-span-5 lg:col-span-5 flex h-full',
};"""

content = re.sub(old_classes, new_classes, content)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)

