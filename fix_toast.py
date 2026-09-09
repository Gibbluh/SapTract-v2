import re

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

# Add import toast from 'react-hot-toast';
if "import toast" not in content:
    content = re.sub(
        r"(import AddUnitModal from './components/AddUnitModal';)", 
        r"\1\nimport toast from 'react-hot-toast';", 
        content
    )

# Replace the onSave callback to also trigger a toast
old_callback = "onSave={(newUnit) => setUnitsList([newUnit, ...unitsList])}"
new_callback = """onSave={(newUnit) => {
          setUnitsList([newUnit, ...unitsList]);
          toast.success(`Unit ${newUnit.plateNumber} added successfully`);
        }}"""

content = content.replace(old_callback, new_callback)

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "w") as f:
    f.write(content)

