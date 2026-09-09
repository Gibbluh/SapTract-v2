import re

with open('frontend/src/pages/admin/MaintenanceDashboard.jsx', 'r') as f:
    content = f.read()

content = content.replace(
    "const highlightId = location.state?.highlightId;",
    "const highlightId = location.state?.highlightId;\n  const effectiveHighlightId = (highlightId && String(highlightId).startsWith('m') && records?.length > 0) ? records[0]._id : highlightId;"
)

content = content.replace(
    "[highlightId, loading, records]",
    "[effectiveHighlightId, loading, records]"
)

content = content.replace(
    "if (highlightId && !loading && records.length > 0) {",
    "if (effectiveHighlightId && !loading && records.length > 0) {"
)

content = content.replace(
    "const el = document.getElementById(`maintenance-row-${highlightId}`);",
    "setTimeout(() => {\n        const el = document.getElementById(`maintenance-row-${effectiveHighlightId}`);\n        if (el) {\n          el.scrollIntoView({ behavior: 'smooth', block: 'center' });\n        }\n      }, 300);"
)

content = content.replace(
    """setTimeout(() => {
        const el = document.getElementById(`maintenance-row-${effectiveHighlightId}`);
        if (el) {
          el.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
      }, 300);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }""",
    """setTimeout(() => {
        const el = document.getElementById(`maintenance-row-${effectiveHighlightId}`);
        if (el) {
          el.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
      }, 300);"""
)

# Update row class ID matching
content = content.replace(
    "highlightId === rec._id",
    "effectiveHighlightId === rec._id"
)

# Add pulsing highlight to row for better visibility
content = content.replace(
    "bg-blue-100 ring-2 ring-inset ring-blue-500 shadow-md",
    "bg-blue-100 ring-2 ring-inset ring-blue-500 shadow-md animate-pulse"
)


with open('frontend/src/pages/admin/MaintenanceDashboard.jsx', 'w') as f:
    f.write(content)
