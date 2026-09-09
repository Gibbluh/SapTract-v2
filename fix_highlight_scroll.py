with open('frontend/src/pages/admin/RemittanceMonitoringPage.jsx', 'r') as f:
    content_remit = f.read()

bad_remit_effect = """  useEffect(() => {
    if (effectiveHighlightId && !loading && remittances.length > 0) {
      setTimeout(() => {
        const el = document.getElementById(`remittance-row-${effectiveHighlightId}`);
        if (el) {
          el.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
      }, 300);
    }
  }, [effectiveHighlightId, loading, remittances]);"""

good_remit_effect = """  useEffect(() => {
    if (effectiveHighlightId && !loading && remittances.length > 0) {
      let attempts = 0;
      const interval = setInterval(() => {
        const el = document.getElementById(`remittance-row-${effectiveHighlightId}`);
        if (el) {
          el.scrollIntoView({ behavior: 'smooth', block: 'center' });
          clearInterval(interval);
        }
        attempts++;
        if (attempts > 20) clearInterval(interval); // give up after 2 seconds
      }, 100);
      return () => clearInterval(interval);
    }
  }, [effectiveHighlightId, loading, remittances.length]);"""

if "const interval = setInterval" not in content_remit:
    if bad_remit_effect in content_remit:
        content_remit = content_remit.replace(bad_remit_effect, good_remit_effect)
    else:
        # Just insert it after setForm
        insert_point = content_remit.find('  useEffect(() => {\n    if (fuelTransaction) {')
        content_remit = content_remit[:insert_point] + good_remit_effect + "\n\n" + content_remit[insert_point:]
        
    with open('frontend/src/pages/admin/RemittanceMonitoringPage.jsx', 'w') as f:
        f.write(content_remit)


with open('frontend/src/pages/admin/MaintenanceDashboard.jsx', 'r') as f:
    content_main = f.read()

good_main_effect = """  useEffect(() => {
    if (effectiveHighlightId && !loading && records.length > 0) {
      let attempts = 0;
      const interval = setInterval(() => {
        const el = document.getElementById(`maintenance-row-${effectiveHighlightId}`);
        if (el) {
          el.scrollIntoView({ behavior: 'smooth', block: 'center' });
          clearInterval(interval);
        }
        attempts++;
        if (attempts > 20) clearInterval(interval); // give up after 2 seconds
      }, 100);
      return () => clearInterval(interval);
    }
  }, [effectiveHighlightId, loading, records.length]);"""

if "const interval = setInterval" not in content_main:
    # Insert it after the first useEffect (like fetchRecords)
    insert_point = content_main.find('  useEffect(() => {\n    fetchDropdowns();\n  }, []);')
    if insert_point == -1:
        insert_point = content_main.find('  useEffect(() => {')
    
    content_main = content_main[:insert_point] + good_main_effect + "\n\n" + content_main[insert_point:]
    
    with open('frontend/src/pages/admin/MaintenanceDashboard.jsx', 'w') as f:
        f.write(content_main)

