with open('frontend/src/pages/admin/MaintenanceDashboard.jsx', 'r') as f:
    content = f.read()

content = content.replace(
    "const effectiveHighlightId = (highlightId && String(highlightId).startsWith('m') && records?.length > 0) ? records[0]._id : highlightId;",
    "// effectiveHighlightId computed below"
)

old_state = """  const [records, setRecords] = useState([]);"""
new_state = """  const [records, setRecords] = useState([]);
  const effectiveHighlightId = (highlightId && String(highlightId).startsWith('m') && records?.length > 0) ? records[0]._id : highlightId;"""

content = content.replace(old_state, new_state)

# Also fix the import location (put it at the top)
content = content.replace(
    'import { useUnitApi } from "../../lib/unitApi";\nimport { useUserApi } from "../../lib/userApi";',
    'import { useUnitApi } from "../../lib/unitApi";\nimport { useUserApi } from "../../lib/userApi";\nimport { useLocation } from "react-router-dom";'
)
content = content.replace(
    '\nimport { useLocation } from "react-router-dom";\n\nconst MaintenanceDashboard = () => {',
    '\nconst MaintenanceDashboard = () => {'
)


with open('frontend/src/pages/admin/MaintenanceDashboard.jsx', 'w') as f:
    f.write(content)
