with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

# I removed a closing div from before `</header>` possibly. Let's look around `<Plus className="w-4 h-4" /> Add Unit`
content = content.replace(
    """        </div>
      </header>""",
    """        </div>
        </div>
      </header>"""
)

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "w") as f:
    f.write(content)
