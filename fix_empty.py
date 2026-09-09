import re

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

# Add empty state right after {/* Grid View */} or before rendering viewMode
empty_state_html = """
        {filteredUnits.length === 0 ? (
          <div className="flex flex-col items-center justify-center p-12 bg-white rounded-xl border border-dashed border-gray-300 text-center">
            <div className="w-16 h-16 bg-gray-50 rounded-2xl flex items-center justify-center mb-4 border border-gray-100">
              <Truck className="w-8 h-8 text-gray-400" />
            </div>
            <h3 className="text-lg font-bold text-gray-900 mb-2">No units found</h3>
            <p className="text-gray-500 max-w-sm mb-6 text-sm">
              {searchQuery || statusFilter !== 'All' || routeFilter !== 'All' 
                ? "We couldn't find any units matching your current filters. Try adjusting your search."
                : "Your fleet is currently empty. Add your first unit to start managing them."}
            </p>
            {(!searchQuery && statusFilter === 'All' && routeFilter === 'All') && (
              <button 
                onClick={() => setFormOpen(true)}
                className="px-5 py-2.5 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700 transition-colors shadow-sm flex items-center gap-2"
              >
                <Plus className="w-4 h-4" /> Add your first unit
              </button>
            )}
          </div>
        ) : (
"""

pattern = r'(\{\/\* Grid View \*\/\}[\s\S]*?\{viewMode === \'grid\' && \()'
content = re.sub(pattern, empty_state_html + r'\1', content)

# Close the ternary expression before pagination
pagination_pattern = r'(        \{\/\* Pagination \*\/\}[\s\S]*?\<div className=\"flex items-center justify-between mt-6\"\>)'
content = re.sub(pagination_pattern, r'        )}\n\n' + r'\1', content)

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "w") as f:
    f.write(content)

