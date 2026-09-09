import re

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

# Replace everything from {formOpen && ( down to export default UnitManagementPage;
match = re.search(r'\{formOpen && \([\s\S]*?export default UnitManagementPage;', content)

replacement = """      <AddUnitModal 
        isOpen={formOpen} 
        onClose={() => setFormOpen(false)} 
        onSave={(newUnit) => {
          setUnitsList([newUnit, ...unitsList]);
          toast.success(`Unit ${newUnit.plateNumber} added successfully`);
        }} 
      />

    </div>
  );
};

export default UnitManagementPage;"""

content = re.sub(r'\{formOpen && \([\s\S]*?export default UnitManagementPage;', replacement, content)

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "w") as f:
    f.write(content)

