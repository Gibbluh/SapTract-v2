with open("frontend/src/pages/admin/components/AddUnitModal.jsx", "r") as f:
    content = f.read()

content = content.replace(
"""          </div>
        </div>

        {/* Modal Footer */}""", 
"""            </div>
          </div>
        </div>

        {/* Modal Footer */}""")

with open("frontend/src/pages/admin/components/AddUnitModal.jsx", "w") as f:
    f.write(content)
