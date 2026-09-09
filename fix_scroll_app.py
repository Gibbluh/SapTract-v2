import re

with open("frontend/src/App.jsx", "r") as f:
    content = f.read()

# Make the main container overflow-y-auto
content = content.replace('<main className="flex-1 min-w-0 min-h-0">', '<main className="flex-1 min-w-0 min-h-0 overflow-y-auto">')

with open("frontend/src/App.jsx", "w") as f:
    f.write(content)

print("Scroll fixed App.jsx")
