with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

lines = content.split("\n")
for i, line in enumerate(lines):
    if "Jeepneys" in line or "Search plate" in line or "Grid View" in line:
        print(f"{i+1}: {line}")
