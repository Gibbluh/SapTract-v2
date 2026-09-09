with open('frontend/src/components/layout/Topbar.jsx', 'r') as f:
    content = f.read()

# We can remove the `<div className="h-6 w-px bg-current opacity-20 hidden sm:block" />` separator since nothing follows it.
content = content.replace('<div className="h-6 w-px bg-current opacity-20 hidden sm:block" />\n        </div>', '        </div>')

with open('frontend/src/components/layout/Topbar.jsx', 'w') as f:
    f.write(content)
