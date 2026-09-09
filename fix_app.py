import re

with open('frontend/src/App.jsx', 'r') as f:
    content = f.read()

content = re.sub(
    r'\{\s*isAuthenticated\s*&&\s*!isPublicDashboard\s*&&\s*\(\s*<button.*?</button>\s*\)\s*\}',
    '{isAuthenticated && !isPublicDashboard && <QuickActionBar />}',
    content,
    flags=re.DOTALL
)

with open('frontend/src/App.jsx', 'w') as f:
    f.write(content)

