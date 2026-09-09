import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

placeholder_regex = r"if \(isDragging\) \{\n\s+return \(\n\s+<div \n\s+ref=\{setNodeRef\} \n\s+style=\{style\} \n\s+className=\{(.*?)\}\n\s+/>\n\s+\);\n\s+\}"
new_placeholder = """if (isDragging) {
    return (
      <div 
        ref={setNodeRef} 
        className={`border-2 border-dashed border-blue-400 dark:border-blue-500 bg-blue-50/50 dark:bg-blue-900/20 rounded-3xl opacity-50 ${className || ''}`}
      />
    );
  }"""
content = re.sub(placeholder_regex, new_placeholder, content, flags=re.DOTALL)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
