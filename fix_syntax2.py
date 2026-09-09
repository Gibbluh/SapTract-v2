import re

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

# Replace the specific block
old_block = """          </div>
        )}

        {/* PAGINATION */}"""

new_block = """          </div>
        )}
          </>
        )}

        {/* PAGINATION */}"""

content = content.replace(old_block, new_block)

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "w") as f:
    f.write(content)
