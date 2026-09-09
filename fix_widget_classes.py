import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# Fix WIDGET_CLASSES
content = content.replace(
    "'chart-weekly-earnings': 'col-span-12 flex h-full min-h-[350px]',",
    "'chart-weekly-earnings': 'col-span-12 lg:col-span-4 flex h-full min-h-[350px]',"
)

# Fix widgetOrder
content = content.replace(
    "'chart-revenue', 'chart-dispatches', 'chart-fleet', 'metric-revenue', 'metric-fuel', 'chart-weekly-earnings'",
    "'chart-revenue', 'chart-weekly-earnings', 'chart-dispatches', 'metric-revenue', 'metric-fuel', 'chart-fleet'"
)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
