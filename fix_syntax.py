import re

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

# Let's find exactly where formOpen is and replace the whole block up to the end of the file.
# The component ends at `export default UnitManagementPage;`
match = re.search(r'\{formOpen && \([\s\S]*?export default UnitManagementPage;', content)

if match:
    pass

# Wait, let's just use regex to replace everything from {formOpen && ( up to export default UnitManagementPage;
replacement = """{formOpen && (
        <div className="absolute inset-0 z-50 flex items-center justify-center p-4">
          <div className="absolute inset-0 bg-gray-900/40 backdrop-blur-sm" onClick={() => setFormOpen(false)}></div>
          <div className="bg-white rounded-2xl w-full max-w-xl flex flex-col relative shadow-2xl animate-in fade-in zoom-in-95">
            <div className="p-6 border-b border-gray-100 flex items-center justify-between shrink-0">
              <h2 className="text-xl font-bold text-gray-900">Add New Unit</h2>
              <button onClick={() => setFormOpen(false)} className="p-2 hover:bg-gray-100 rounded-full transition-colors text-gray-500"><X className="w-5 h-5"/></button>
            </div>
            <form onSubmit={(e) => {
              e.preventDefault();
              const formData = new FormData(e.target);
              const newUnit = {
                id: `UNT-2024-${String(unitsList.length + 1).padStart(3, '0')}`,
                plateNumber: formData.get('plateNumber'),
                unitNumber: formData.get('unitNumber'),
                make: formData.get('make'),
                model: formData.get('model'),
                year: formData.get('year'),
                type: formData.get('type'),
                capacity: parseInt(formData.get('capacity')),
                route: formData.get('route'),
                status: 'Available',
                registrationExpiry: new Date(new Date().setFullYear(new Date().getFullYear() + 1)).toISOString().split('T')[0],
                insuranceExpiry: new Date(new Date().setFullYear(new Date().getFullYear() + 1)).toISOString().split('T')[0],
                maintenanceStatus: 'Good',
                driver: 'Unassigned',
                conductor: 'Unassigned'
              };
              setUnitsList([newUnit, ...unitsList]);
              setFormOpen(false);
            }}>
              <div className="p-6 overflow-y-auto max-h-[60vh] flex flex-col gap-4">
                 <div className="grid grid-cols-2 gap-4">
                   <div>
                     <label className="block text-sm font-medium text-gray-700 mb-1">Unit Number (ID)</label>
                     <input required name="unitNumber" type="text" className="w-full border border-gray-300 rounded-lg p-2 text-sm focus:ring-2 focus:ring-blue-500 outline-none" placeholder="e.g. 101" />
                   </div>
                   <div>
                     <label className="block text-sm font-medium text-gray-700 mb-1">Plate Number</label>
                     <input required name="plateNumber" type="text" className="w-full border border-gray-300 rounded-lg p-2 text-sm focus:ring-2 focus:ring-blue-500 outline-none" placeholder="ABC-1234" />
                   </div>
                   <div>
                     <label className="block text-sm font-medium text-gray-700 mb-1">Make</label>
                     <input required name="make" type="text" className="w-full border border-gray-300 rounded-lg p-2 text-sm focus:ring-2 focus:ring-blue-500 outline-none" placeholder="Toyota" />
                   </div>
                   <div>
                     <label className="block text-sm font-medium text-gray-700 mb-1">Model</label>
                     <input required name="model" type="text" className="w-full border border-gray-300 rounded-lg p-2 text-sm focus:ring-2 focus:ring-blue-500 outline-none" placeholder="Hiace Commuter" />
                   </div>
                   <div>
                     <label className="block text-sm font-medium text-gray-700 mb-1">Year</label>
                     <input required name="year" type="number" className="w-full border border-gray-300 rounded-lg p-2 text-sm focus:ring-2 focus:ring-blue-500 outline-none" placeholder="2024" defaultValue="2024" />
                   </div>
                   <div>
                     <label className="block text-sm font-medium text-gray-700 mb-1">Type</label>
                     <select name="type" className="w-full border border-gray-300 rounded-lg p-2 text-sm focus:ring-2 focus:ring-blue-500 outline-none">
                       <option>Van</option>
                       <option>Minibus</option>
                       <option>Jeepney</option>
                     </select>
                   </div>
                   <div>
                     <label className="block text-sm font-medium text-gray-700 mb-1">Capacity</label>
                     <input required name="capacity" type="number" className="w-full border border-gray-300 rounded-lg p-2 text-sm focus:ring-2 focus:ring-blue-500 outline-none" placeholder="15" defaultValue="15" />
                   </div>
                   <div>
                     <label className="block text-sm font-medium text-gray-700 mb-1">Route Assignment</label>
                     <select name="route" className="w-full border border-gray-300 rounded-lg p-2 text-sm focus:ring-2 focus:ring-blue-500 outline-none">
                       <option value="UNASSIGNED">Unassigned</option>
                       <option value="LANGGAM">Langgam</option>
                       <option value="VILLAROSA">Villarosa</option>
                       <option value="BAYAN-BAYANAN">Bayan-Bayanan</option>
                       <option value="ESTRELLA">Estrella</option>
                       <option value="CALAMBA">Calamba</option>
                     </select>
                   </div>
                 </div>
              </div>
              <div className="p-4 border-t border-gray-100 bg-gray-50 flex justify-end gap-3 rounded-b-2xl shrink-0">
                <button type="button" onClick={() => setFormOpen(false)} className="px-4 py-2 font-medium text-gray-600 hover:text-gray-900 transition-colors">Cancel</button>
                <button type="submit" className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg shadow-sm transition-colors">Save Unit</button>
              </div>
            </form>
          </div>
        </div>
      )}

    </div>
  );
};

export default UnitManagementPage;"""

content = re.sub(r'\{formOpen && \([\s\S]*?export default UnitManagementPage;', replacement, content)

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "w") as f:
    f.write(content)
