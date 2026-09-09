import re

with open('frontend/src/pages/admin/DriverManagementPage.jsx', 'r') as f:
    content = f.read()

# Make Bulk Actions match prompt
bulk_search = r'<button className="text-sm font-medium hover:text-blue-100 transition-colors">Assign Route</button>\s*<button className="text-sm font-medium hover:text-blue-100 transition-colors">Change Status</button>\s*<button className="text-sm font-medium hover:text-blue-100 transition-colors">Generate QR</button>'
bulk_replace = r'<button className="text-sm font-medium hover:text-blue-100 transition-colors">Change Status</button>\n            <button className="text-sm font-medium hover:text-blue-100 transition-colors">Download QRs</button>\n            <button className="text-sm font-medium hover:text-blue-100 transition-colors">Export (CSV)</button>\n            <button className="text-sm font-medium hover:text-red-300 transition-colors">Archive</button>'

content = re.sub(bulk_search, bulk_replace, content)

with open('frontend/src/pages/admin/DriverManagementPage.jsx', 'w') as f:
    f.write(content)
