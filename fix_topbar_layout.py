import re

with open('frontend/src/components/layout/Topbar.jsx', 'r') as f:
    content = f.read()

# Let's check how the Topbar finishes its right side div
# Search for Real-Time Notification Bell
bell_regex = r"          \{/\* Real-Time Notification Bell \*/\}.*?          </div>"
match = re.search(bell_regex, content, flags=re.DOTALL)
if match:
    pass

