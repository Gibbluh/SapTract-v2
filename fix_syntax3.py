with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

marker = '          </div>\n        </div>'
parts = content.split(marker)
# The garbage is right after the second '        </div>' in chart-dispatches. Let's find it.

# Let's use re with a broad pattern
import re

# find the exact garbage block
garbage = r'        <div className="flex items-center justify-between mt-3 pt-3 border-t dark:border-slate-700 border-slate-200/60">.*?</div>\s*</div>\s*\)\}\)\}\s*</div>\s*</div>'

content = re.sub(garbage, '', content, flags=re.DOTALL)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
