import re

with open('frontend/src/pages/admin/UnitManagementPage.jsx', 'r') as f:
    content = f.read()

# 1. Remove selectedUnits state
content = re.sub(r'const \[selectedUnits, setSelectedUnits\] = useState\(new Set\(\)\);\n', '', content)

# 2. Remove toggleSelection and toggleAll functions
content = re.sub(r'const toggleSelection = \(id\) => \{.*?\};\n\n  const toggleAll = \(\) => \{.*?\};\n', '', content, flags=re.DOTALL)

# 3. Remove Bulk Action Bar
content = re.sub(r'\{\s*selectedUnits\.size > 0 && \(\s*<div className="absolute top-6 left-1/2.*?</div>\s*\)\s*\}\s*', '', content, flags=re.DOTALL)

# 4. Remove Table Header Checkbox
content = re.sub(r'<th className="px-4 py-3 w-10">\s*<input\s*type="checkbox".*?onChange=\{toggleAll\}.*?/>\s*</th>', '', content, flags=re.DOTALL)

# 5. Remove Table Row Checkbox
content = re.sub(r'<td className="px-4 py-3">\s*<div className="flex items-center" onClick=\{e => e\.stopPropagation\(\)\}>\s*<input\s*type="checkbox".*?onChange=\{.*?toggleSelection\(unit\.id\).*?/>\s*</div>\s*</td>', '', content, flags=re.DOTALL)

# 6. Update row onClick
content = content.replace("if (e.target.type !== 'checkbox' && !e.target.closest('button'))", "if (!e.target.closest('button'))")

# 7. Decrease colSpan from 7 to 6 if exists
content = content.replace('colSpan="7"', 'colSpan="6"').replace('colSpan={7}', 'colSpan={6}')

with open('frontend/src/pages/admin/UnitManagementPage.jsx', 'w') as f:
    f.write(content)
