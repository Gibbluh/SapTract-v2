import re

with open('frontend/src/components/layout/Sidebar.jsx', 'r') as f:
    content = f.read()

# Remove the Logout Button block from the Sidebar
logout_regex = r"          \{/\* Logout Button \*/\}.*?</button>"
content = re.sub(logout_regex, "", content, flags=re.DOTALL)

# Speed up the main sidebar transitions to feel less laggy (duration-300 -> duration-200)
content = content.replace('transition-[width,box-shadow] duration-300 ease-in-out', 'transition-[width,box-shadow] duration-150 ease-out')
content = content.replace('transition-[width] duration-300 ease-in-out', 'transition-[width] duration-150 ease-out')
content = content.replace('transition-all duration-300 ease-in-out', 'transition-all duration-150 ease-out')

with open('frontend/src/components/layout/Sidebar.jsx', 'w') as f:
    f.write(content)
