with open('frontend/src/pages/admin/MaintenanceDashboard.jsx', 'r') as f:
    content = f.read()

old_use_auth = """  const { user } = useAuth();
  const { fetchRecords, records, loading, error, createRecord, addStatusUpdate } = useMaintenanceApi();"""

new_use_auth = """  const { user } = useAuth();
  const { fetchRecords, records, loading, error, createRecord, addStatusUpdate } = useMaintenanceApi();

  useEffect(() => {
    if (highlightId && !loading && records.length > 0) {
      const el = document.getElementById(`maintenance-row-${highlightId}`);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }
  }, [highlightId, loading, records]);"""

if "el.scrollIntoView" not in content:
    content = content.replace(old_use_auth, new_use_auth)

with open('frontend/src/pages/admin/MaintenanceDashboard.jsx', 'w') as f:
    f.write(content)
