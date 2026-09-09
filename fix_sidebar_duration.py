import re

with open('frontend/src/components/layout/Sidebar.jsx', 'r') as f:
    content = f.read()

# Change all duration-300 to duration-100
content = content.replace('duration-300', 'duration-150')
content = content.replace('ease-in-out', 'ease-out')
# Make the layout spacer not animate width slowly
content = content.replace('transition-[width] duration-150 ease-out relative', 'transition-[width] duration-100 ease-out relative')
# Main aside container
content = content.replace('transition-[width,box-shadow] duration-150 ease-out', 'transition-[width,box-shadow] duration-100 ease-out')
# Text max-w transition
content = content.replace('transition-all duration-150 ease-out', 'transition-all duration-100 ease-out')

with open('frontend/src/components/layout/Sidebar.jsx', 'w') as f:
    f.write(content)
