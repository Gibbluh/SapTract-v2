import re

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

empty_state_html = """        {filteredUnits.length === 0 ? (
          <div className="flex flex-col items-center justify-center p-12 bg-white rounded-xl border border-dashed border-gray-300 text-center mb-6">
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
          <>
            {viewMode === 'grid' ? ("""

content = content.replace("{viewMode === 'grid' ? (", empty_state_html)

# Now we need to close the <> right before Pagination
# Pagination starts with: {/* Pagination */}
close_empty = """
          </>
        )}

        {/* Pagination */"""

content = content.replace("{/* Pagination */", close_empty)

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "w") as f:
    f.write(content)

