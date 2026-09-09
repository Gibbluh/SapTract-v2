import os
import re

for root, _, files in os.walk('frontend/src/pages'):
    for file in files:
        if file.endswith('.jsx'):
            path = os.path.join(root, file)
            with open(path, 'r') as f:
                content = f.read()

            if "toast(" in content or "toast\n" in content:
                # Replace toast("...successfully...") with toast.success
                content = re.sub(r'toast\((.*?successfully.*?)\)', r'toast.success(\1)', content)
                # For remaining generic toasts that contain typical error words, use toast.error
                content = re.sub(r'toast\((.*?(required|failed|Invalid|error|Error|Failed).*?)\)', r'toast.error(\1)', content)

                with open(path, 'w') as f:
                    f.write(content)
