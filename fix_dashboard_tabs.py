import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# Update Revenue Overview tabs
old_revenue_tabs = """{['Today', 'Last Week', 'Last Month'].map(tab => ("""
new_revenue_tabs = """{['1d', '1w', '1m', '6m', '1y'].map(tab => ("""
content = content.replace(old_revenue_tabs, new_revenue_tabs)

# Default revenue tab
content = content.replace("const [revenueTab, setRevenueTab] = useState('Today');", "const [revenueTab, setRevenueTab] = useState('1d');")

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
