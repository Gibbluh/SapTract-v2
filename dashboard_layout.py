import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# 1. Layout rearrangement
old_classes = r"""const WIDGET_CLASSES = \{
  'metric-revenue': 'col-span-12 sm:col-span-6 h-full flex',
  'metric-fuel': 'col-span-12 sm:col-span-6 h-full flex',
  'chart-revenue': 'col-span-12 lg:col-span-8 flex h-full',
  'chart-fleet': 'col-span-12 lg:col-span-4 flex h-full',
  'chart-dispatches': 'col-span-12 lg:col-span-12 flex h-full' // Changed to full width to fit leaderboard nicely
\};"""

new_classes = """const WIDGET_CLASSES = {
  'chart-revenue': 'col-span-12 lg:col-span-8 lg:row-span-2 flex h-full min-h-[400px]',
  'chart-dispatches': 'col-span-12 lg:col-span-4 flex h-full max-h-[500px]',
  'chart-fleet': 'col-span-12 lg:col-span-4 flex h-full',
  'metric-revenue': 'col-span-12 sm:col-span-6 lg:col-span-4 flex h-full',
  'metric-fuel': 'col-span-12 sm:col-span-6 lg:col-span-4 flex h-full',
};"""

content = re.sub(old_classes, new_classes, content)

old_order = r"""  const \[widgetOrder, setWidgetOrder\] = useState\(\[
    'metric-revenue', 'metric-fuel',
    'chart-revenue', 'chart-fleet', 'chart-dispatches'
  \]\);"""

new_order = """  const [widgetOrder, setWidgetOrder] = useState([
    'chart-revenue', 'chart-dispatches', 'chart-fleet', 'metric-revenue', 'metric-fuel'
  ]);"""

content = re.sub(old_order, new_order, content)

# 2. Fix the main grid to allow row-spanning and dense packing
# The main grid container is: <div className="grid grid-cols-1 md:grid-cols-12 gap-4 lg:gap-6 pb-20">
content = content.replace(
    '<div className="grid grid-cols-1 md:grid-cols-12 gap-4 lg:gap-6 pb-20">',
    '<div className="grid grid-cols-1 md:grid-cols-12 gap-4 lg:gap-6 pb-20 grid-flow-row-dense">'
)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)

