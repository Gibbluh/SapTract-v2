import re

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "r") as f:
    content = f.read()

# Replace the Checkbox in Grid View
grid_checkbox_pattern = r'<div\s+onClick=\{\(e\) => toggleSelection\(unit\.id, e\)\}\s+className=\{`absolute top-3 left-3 z-10 p-1\.5 rounded-md transition-opacity.*?`\}\s*>\s*<input\s+type="checkbox"\s+checked=\{isSelected\}\s+readOnly\s+className="[^"]+"\s*/>\s*</div>'
grid_checkbox_replacement = """<div 
                    onClick={(e) => toggleSelection(unit.id, e)}
                    className={`absolute top-3 left-3 z-10 p-1.5 rounded-md transition-opacity 
                      ${isSelected ? 'opacity-100 bg-white/90 shadow-sm' : 'opacity-0 group-hover:opacity-100 bg-white/70 hover:bg-white'}
                    `}
                  >
                    <input 
                      type="checkbox" 
                      checked={isSelected}
                      readOnly
                      className="checkbox checkbox-sm checkbox-primary rounded border-gray-300"
                    />
                  </div>"""

content = re.sub(grid_checkbox_pattern, grid_checkbox_replacement, content, flags=re.DOTALL)


# Replace the Header Checkbox
header_th_pattern = r'<th className="px-4 py-3 w-10">\s*<input\s+type="checkbox"\s+className="[^"]+"\s+checked=\{selectedUnits\.size === paginatedUnits\.length && paginatedUnits\.length > 0\}\s+onChange=\{toggleAll\}\s*/>\s*</th>'
header_th_replacement = """<th className="pl-5 pr-2 py-3 w-10">
                      <input 
                        type="checkbox" 
                        className="checkbox checkbox-sm checkbox-primary rounded border-gray-300"
                        checked={selectedUnits.size === paginatedUnits.length && paginatedUnits.length > 0}
                        onChange={toggleAll}
                      />
                    </th>"""

content = re.sub(header_th_pattern, header_th_replacement, content)

# Modify the next header
content = content.replace('<th className="px-4 py-3">Unit</th>', '<th className="pl-2 pr-4 py-3">Unit</th>')

# Replace the Row Checkbox
row_td_pattern = r'<td className="px-4 py-3" onClick=\{\(e\) => toggleSelection\(unit\.id, e\)\}>\s*<input\s+type="checkbox"\s+checked=\{isSelected\}\s+readOnly\s+className="[^"]+"\s*/>\s*</td>'
row_td_replacement = """<td className="pl-5 pr-2 py-3" onClick={(e) => toggleSelection(unit.id, e)}>
                          <input 
                            type="checkbox" 
                            checked={isSelected}
                            readOnly
                            className="checkbox checkbox-sm checkbox-primary rounded border-gray-300"
                          />
                        </td>"""
content = re.sub(row_td_pattern, row_td_replacement, content)

# Modify the next td
content = content.replace('<td className="px-4 py-3">\n                          <div className="flex items-center gap-3">', '<td className="pl-2 pr-4 py-3">\n                          <div className="flex items-center gap-3">')

with open("frontend/src/pages/admin/UnitManagementPage.jsx", "w") as f:
    f.write(content)
print("Checkboxes updated.")
