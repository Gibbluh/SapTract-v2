import re

with open('frontend/src/pages/admin/UnitManagementPage.jsx', 'r') as f:
    content = f.read()

# 1. Remove toggleSelection and toggleAll
content = re.sub(r'const toggleSelection = \(id\) => \{.*?\};\s*const toggleAll = \(\) => \{.*?\};\s*', '', content, flags=re.DOTALL)

# 2. Remove any remaining th with checkbox (just in case)
content = re.sub(r'<th className="px-4 py-3 w-10">.*?</th>\s*', '', content, flags=re.DOTALL)

# 3. Remove any remaining td with checkbox
content = re.sub(r'<td className="px-4 py-3">\s*<input[^>]+type="checkbox"[^>]+/>\s*</td>\s*', '', content, flags=re.DOTALL)
content = re.sub(r'<td className="px-4 py-3">\s*<div className="flex items-center"[^>]*>\s*<input[^>]+type="checkbox"[^>]+/>\s*</div>\s*</td>\s*', '', content, flags=re.DOTALL)

with open('frontend/src/pages/admin/UnitManagementPage.jsx', 'w') as f:
    f.write(content)
