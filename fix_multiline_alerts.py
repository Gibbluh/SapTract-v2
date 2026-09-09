import os
import re

for root, _, files in os.walk('frontend/src'):
    for file in files:
        if file.endswith('.jsx'):
            path = os.path.join(root, file)
            with open(path, 'r') as f:
                content = f.read()

            if "alert(" in content or "window.alert(" in content:
                # Add import if not present
                toast_import = "import toast from 'react-hot-toast';"
                if toast_import not in content:
                    imports_end = content.rfind('import ')
                    if imports_end != -1:
                        next_line = content.find('\n', imports_end)
                        content = content[:next_line] + f"\n{toast_import}" + content[next_line:]
                    else:
                        content = f"{toast_import}\n" + content

                # Replace multiline alert
                content = re.sub(r'window\.alert\((.*?)\)', r'toast.error(\1)', content, flags=re.DOTALL)
                content = re.sub(r'alert\((.*?)\)', r'toast.error(\1)', content, flags=re.DOTALL)

                with open(path, 'w') as f:
                    f.write(content)
