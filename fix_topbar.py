with open("frontend/src/components/layout/Topbar.jsx", "r") as f:
    content = f.read()

content = content.replace("location.pathname === '/units' ? 'invisible'", "['/units', '/dashboard', '/drivers'].includes(location.pathname) ? 'invisible'")

with open("frontend/src/components/layout/Topbar.jsx", "w") as f:
    f.write(content)
