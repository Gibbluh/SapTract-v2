with open('frontend/src/lib/ThemeContext.jsx', 'r') as f:
    content = f.read()

old_effect = """  useEffect(() => {
    localStorage.setItem("app-theme", theme);
    document.body.setAttribute("data-app-theme", theme);
  }, [theme]);"""

new_effect = """  useEffect(() => {
    localStorage.setItem("app-theme", theme);
    document.body.setAttribute("data-app-theme", theme);
    if (theme === 'theme-5') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [theme]);"""

if old_effect in content:
    content = content.replace(old_effect, new_effect)
else:
    # try one-liner replace if formatting is weird
    import re
    content = re.sub(r'document\.body\.setAttribute\("data-app-theme", theme\);\s*\}, \[theme\]\);', 
                     'document.body.setAttribute("data-app-theme", theme); if (theme === "theme-5") { document.documentElement.classList.add("dark"); } else { document.documentElement.classList.remove("dark"); } }, [theme]);',
                     content)

with open('frontend/src/lib/ThemeContext.jsx', 'w') as f:
    f.write(content)

