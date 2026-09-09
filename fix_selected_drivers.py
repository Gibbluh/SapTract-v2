with open('frontend/src/pages/admin/DriverManagementPage.jsx', 'r') as f:
    content = f.read()

content = content.replace("  const [selectedDrivers, setSelectedDrivers] = useState(new Set());\n", "")

with open('frontend/src/pages/admin/DriverManagementPage.jsx', 'w') as f:
    f.write(content)
