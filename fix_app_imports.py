import re

with open('frontend/src/App.jsx', 'r') as f:
    content = f.read()

# Add import if not present
if 'QuickActionBar' not in content[:1000]:
    content = content.replace(
        'import Topbar from "./components/layout/Topbar";',
        'import Topbar from "./components/layout/Topbar";\nimport QuickActionBar from "./components/layout/QuickActionBar";'
    )

with open('frontend/src/App.jsx', 'w') as f:
    f.write(content)
