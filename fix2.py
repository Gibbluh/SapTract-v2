import re

with open('frontend/src/pages/admin/UnitManagementPage.jsx', 'r') as f:
    content = f.read()

# Just rip out the specific td block for the row checkbox
content = re.sub(r'<td className="px-4 py-3">\s*<input[^>]+type="checkbox"[^>]+/>\s*</td>', '', content, flags=re.DOTALL)

with open('frontend/src/pages/admin/UnitManagementPage.jsx', 'w') as f:
    f.write(content)
