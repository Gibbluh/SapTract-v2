with open('frontend/tailwind.config.js', 'r') as f:
    content = f.read()

if "darkMode:" not in content:
    content = content.replace('theme: {', "darkMode: 'class',\n  theme: {")
    with open('frontend/tailwind.config.js', 'w') as f:
        f.write(content)

