with open('frontend/src/pages/admin/MaintenanceDashboard.jsx', 'r') as f:
    content = f.read()

# Add location and highlightId
old_comp = """const MaintenanceDashboard = () => {
  const { user } = useAuth();
  const { fetchRecords, records, loading, error, createRecord, addStatusUpdate } = useMaintenanceApi();"""

new_comp = """import { useLocation } from "react-router-dom";

const MaintenanceDashboard = () => {
  const location = useLocation();
  const highlightId = location.state?.highlightId;
  const { user } = useAuth();
  const { fetchRecords, records, loading, error, createRecord, addStatusUpdate } = useMaintenanceApi();

  useEffect(() => {
    if (highlightId && !loading && records.length > 0) {
      const el = document.getElementById(`maintenance-row-${highlightId}`);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }
  }, [highlightId, loading, records]);"""

if "import { useLocation } from" not in content:
    content = content.replace(old_comp, new_comp)

# Add highlight class to tr
old_tr = """                      <tr className="border-b border-slate-200 hover:bg-slate-50 transition-colors">"""

new_tr = """                      <tr 
                        id={`maintenance-row-${rec._id}`}
                        className={`border-b transition-all duration-500 ${highlightId === rec._id ? 'bg-blue-100 ring-2 ring-inset ring-blue-500 shadow-md' : 'border-slate-200 hover:bg-slate-50'}`}
                      >"""

content = content.replace(old_tr, new_tr)

with open('frontend/src/pages/admin/MaintenanceDashboard.jsx', 'w') as f:
    f.write(content)

