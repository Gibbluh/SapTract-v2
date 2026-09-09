import re

with open("frontend/src/pages/admin/components/AddUnitModal.jsx", "r") as f:
    content = f.read()

# Make sure all inputs have bg-white and text-gray-900 to prevent them from rendering black in dark mode
content = content.replace("w-full border border-gray-300", "w-full bg-white text-gray-900 border border-gray-300")
content = content.replace("border-red-300", "bg-white text-gray-900 border-red-300")
content = content.replace("w-full border bg-white", "w-full bg-white")
content = content.replace("border-gray-300 focus:ring-blue-500 rounded-lg", "bg-white text-gray-900 border-gray-300 focus:ring-blue-500 rounded-lg")

with open("frontend/src/pages/admin/components/AddUnitModal.jsx", "w") as f:
    f.write(content)

