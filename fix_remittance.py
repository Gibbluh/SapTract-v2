with open('frontend/src/pages/admin/RemittanceMonitoringPage.jsx', 'r') as f:
    content = f.read()

# Add highlightId extraction
old_loc = """  const location = useLocation();
  const fuelTransaction = location.state?.fuelTransaction;"""
new_loc = """  const location = useLocation();
  const fuelTransaction = location.state?.fuelTransaction;
  const highlightId = location.state?.highlightId;
  const effectiveHighlightId = (highlightId && String(highlightId).startsWith('m') && remittances?.length > 0) ? remittances[0]._id : highlightId;"""

if "const highlightId = location.state?.highlightId;" not in content:
    content = content.replace(old_loc, new_loc)

# Add scrolling useEffect
old_use = """  useEffect(() => {
    if (fuelTransaction) {"""

new_use = """  useEffect(() => {
    if (effectiveHighlightId && !loading && remittances.length > 0) {
      setTimeout(() => {
        const el = document.getElementById(`remittance-row-${effectiveHighlightId}`);
        if (el) {
          el.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
      }, 300);
    }
  }, [effectiveHighlightId, loading, remittances]);

  useEffect(() => {
    if (fuelTransaction) {"""

if "effectiveHighlightId && !loading" not in content:
    content = content.replace(old_use, new_use)

# Update RemittanceTable call
old_tab = """        <RemittanceTable
          remittances={remittances}
          loading={loading}
          error={error}
          onVerify={handleVerify}
          page={page}
          totalPages={totalPages}
          onPageChange={setPage}
          highlightId={highlightId}
        />"""
new_tab = """        <RemittanceTable
          remittances={remittances}
          loading={loading}
          error={error}
          onVerify={handleVerify}
          page={page}
          totalPages={totalPages}
          onPageChange={setPage}
          highlightId={effectiveHighlightId}
        />"""
if "highlightId={effectiveHighlightId}" not in content:
    content = content.replace(old_tab, new_tab)
    content = content.replace(
        "        <RemittanceTable\n          remittances={remittances}\n          loading={loading}\n          error={error}\n          onVerify={handleVerify}\n          page={page}\n          totalPages={totalPages}\n          onPageChange={setPage}\n        />",
        "        <RemittanceTable\n          remittances={remittances}\n          loading={loading}\n          error={error}\n          onVerify={handleVerify}\n          page={page}\n          totalPages={totalPages}\n          onPageChange={setPage}\n          highlightId={effectiveHighlightId}\n        />"
    )

with open('frontend/src/pages/admin/RemittanceMonitoringPage.jsx', 'w') as f:
    f.write(content)
