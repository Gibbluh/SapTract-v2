import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# Let's remove the 4 grid boxes in chart-fleet
fleet_bottom_regex = r'          <div className="w-full grid grid-cols-2 gap-3 mb-6 pointer-events-auto">.*?</div>\n            </div>\n          </div>\n        </div>'

# We replace it with just the closing div of the card
new_bottom = """        </div>"""

content = re.sub(fleet_bottom_regex, new_bottom, content, flags=re.DOTALL)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
