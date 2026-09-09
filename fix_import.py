import re

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

# Add import if not present
if "import AddUnitModal" not in content:
    # insert after the lucide-react import
    content = re.sub(
        r"(from 'lucide-react';)", 
        r"\1\nimport AddUnitModal from './components/AddUnitModal';", 
        content
    )

# Replace the form Open block
# Wait, let's use string manipulation because the formOpen block is big
form_open_pattern = r'\{formOpen && \([\s\S]*?\}\s*\)\}'
replacement = """      <AddUnitModal 
        isOpen={formOpen} 
        onClose={() => setFormOpen(false)} 
        onSave={(newUnit) => setUnitsList([newUnit, ...unitsList])} 
      />"""

content = re.sub(form_open_pattern, replacement, content)

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "w") as f:
    f.write(content)

