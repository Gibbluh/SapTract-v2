with open('frontend/src/pages/admin/RemittanceMonitoringPage.jsx', 'r') as f:
    content = f.read()

# 1. Add highlightId to RemittanceTable props
old_table_props = """const RemittanceTable = ({
  remittances,
  loading,
  error,
  onVerify,
  page,
  totalPages,
  onPageChange,
}) => ("""

new_table_props = """const RemittanceTable = ({
  remittances,
  loading,
  error,
  onVerify,
  page,
  totalPages,
  onPageChange,
  highlightId,
}) => ("""

content = content.replace(old_table_props, new_table_props)

# 2. Add highlight class to tr
old_tr = """            <tr
              key={r._id}
              className="border-b border-slate-100 hover:bg-slate-50/55 transition-colors duration-150 odd:bg-white even:bg-slate-50/20"
            >"""

new_tr = """            <tr
              key={r._id}
              className={`border-b transition-all duration-500 ${highlightId === r._id ? 'bg-blue-100 ring-2 ring-inset ring-blue-500 shadow-md' : 'border-slate-100 hover:bg-slate-50/55 odd:bg-white even:bg-slate-50/20'}`}
              id={`remittance-row-${r._id}`}
            >"""

content = content.replace(old_tr, new_tr)

# 3. Add location and pass highlightId in component
old_comp = """const RemittanceMonitoringPage = () => {
  const {
    fetchRemittances,
    remittances,
    loading,
    error,
    verifyRemittance,
  } = useRemittanceApi();"""

new_comp = """const RemittanceMonitoringPage = () => {
  const location = useLocation();
  const highlightId = location.state?.highlightId;
  const {
    fetchRemittances,
    remittances,
    loading,
    error,
    verifyRemittance,
  } = useRemittanceApi();

  useEffect(() => {
    if (highlightId && !loading && remittances.length > 0) {
      const el = document.getElementById(`remittance-row-${highlightId}`);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }
  }, [highlightId, loading, remittances]);"""

content = content.replace(old_comp, new_comp)

# 4. Pass highlightId to RemittanceTable
old_table_usage = """        <RemittanceTable
          remittances={remittances}
          loading={loading}
          error={error}
          onVerify={verifyRemittance}
          page={page}
          totalPages={totalPages}
          onPageChange={setPage}
        />"""

new_table_usage = """        <RemittanceTable
          remittances={remittances}
          loading={loading}
          error={error}
          onVerify={verifyRemittance}
          page={page}
          totalPages={totalPages}
          onPageChange={setPage}
          highlightId={highlightId}
        />"""

content = content.replace(old_table_usage, new_table_usage)

with open('frontend/src/pages/admin/RemittanceMonitoringPage.jsx', 'w') as f:
    f.write(content)

