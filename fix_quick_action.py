with open('frontend/src/components/layout/QuickActionBar.jsx', 'r') as f:
    content = f.read()

content = content.replace(
    'onMouseLeave={() => setIsOpen(false)}',
    'onMouseLeave={() => setIsOpen(false)}\n      onClick={() => setIsOpen(!isOpen)}'
)

with open('frontend/src/components/layout/QuickActionBar.jsx', 'w') as f:
    f.write(content)

