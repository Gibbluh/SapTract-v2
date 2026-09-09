import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# 1. Revert min-h-[400px] to min-h-[350px] on the big charts
content = content.replace("min-h-[400px]", "min-h-[350px]")

# 2. Reduce the maxHeight of the driver list from 380px to 180px
content = content.replace("maxHeight: '380px'", "maxHeight: '180px'")

# 3. Reduce padding/margins in chart-dispatches to make it more compact if needed
# Actually just the maxHeight should be enough to stop it from forcing the row to be huge.

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
