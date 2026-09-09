import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# Make sure chart-fleet does not have a min-h setting that forces it to be tall, we want it compact.
# Also fix chart-dispatches max-h if it's there
content = content.replace("'chart-dispatches': 'col-span-12 lg:col-span-4 flex h-full max-h-[500px]',", "'chart-dispatches': 'col-span-12 lg:col-span-4 flex h-full',")

# Let's adjust the row-spanning slightly.
# We want: 
# Row 1: col 1 = chart-revenue (span 8), col 2 = chart-dispatches (span 4)
# Row 2: col 1 = chart-revenue (span 8, spans from row 1), col 2 = chart-fleet (span 4)
# Row 3: col 1 = metric-revenue (span 6 or 4), col 2 = metric-fuel (span 6 or 4)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
