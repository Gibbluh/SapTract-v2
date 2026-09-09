import re

with open('frontend/src/pages/admin/RemittanceMonitoringPage.jsx', 'r') as f:
    content = f.read()

# Make actualHighlightId handle 'm' prefixed mock IDs
# If it's a mock ID (e.g. 'm1'), it will grab the ID of the first record in the list.
# Thus ensuring the highlighting works even when using the dummy notifications.
content = content.replace(
    "const highlightId = location.state?.highlightId;",
    "const highlightId = location.state?.highlightId;\n  const effectiveHighlightId = (highlightId && String(highlightId).startsWith('m') && remittances?.length > 0) ? remittances[0]._id : highlightId;"
)

# Update useEffect dependencies and logic
content = content.replace(
    "[highlightId, loading, remittances]",
    "[effectiveHighlightId, loading, remittances]"
)

content = content.replace(
    "if (highlightId && !loading && remittances.length > 0) {",
    "if (effectiveHighlightId && !loading && remittances.length > 0) {"
)

content = content.replace(
    "const el = document.getElementById(`remittance-row-${highlightId}`);",
    "setTimeout(() => {\n        const el = document.getElementById(`remittance-row-${effectiveHighlightId}`);\n        if (el) {\n          el.scrollIntoView({ behavior: 'smooth', block: 'center' });\n        }\n      }, 300);"
)

# Fix double if(el) because we injected a block with setTimeout
content = content.replace(
    """setTimeout(() => {
        const el = document.getElementById(`remittance-row-${effectiveHighlightId}`);
        if (el) {
          el.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
      }, 300);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }""",
    """setTimeout(() => {
        const el = document.getElementById(`remittance-row-${effectiveHighlightId}`);
        if (el) {
          el.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
      }, 300);"""
)

content = content.replace(
    "highlightId={highlightId}",
    "highlightId={effectiveHighlightId}"
)

# Add pulsing highlight to row for better visibility
content = content.replace(
    "bg-blue-100 ring-2 ring-inset ring-blue-500 shadow-md",
    "bg-blue-100 ring-2 ring-inset ring-blue-500 shadow-md animate-pulse"
)

with open('frontend/src/pages/admin/RemittanceMonitoringPage.jsx', 'w') as f:
    f.write(content)
