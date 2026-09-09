import re

with open("frontend/src/pages/admin/components/AddUnitModal.jsx", "r") as f:
    content = f.read()

content = content.replace("Image as ImageIcon, ", "")

with open("frontend/src/pages/admin/components/AddUnitModal.jsx", "w") as f:
    f.write(content)
