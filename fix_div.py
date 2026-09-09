import re

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

# Let's find the unclosed div by looking at line 717
lines = content.split('\n')
for i, line in enumerate(lines):
    if i >= 250 and i <= 270:
        pass
