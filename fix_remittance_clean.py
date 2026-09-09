with open('frontend/src/pages/admin/RemittanceMonitoringPage.jsx', 'r') as f:
    content = f.read()

bad_use_effect = """  useEffect(() => {
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
    if (fuelTransaction) {
      setForm({"""

fixed_use_effect = """  useEffect(() => {
    if (fuelTransaction) {
      setForm({"""

content = content.replace(bad_use_effect, fixed_use_effect)

# Fix remittances missing effectiveHighlightId
# Wait, effectiveHighlightId is using `remittances`, but `remittances` is declared AFTER effectiveHighlightId is declared!
# Look at this:
#  const highlightId = location.state?.highlightId;
#  const effectiveHighlightId = (highlightId && String(highlightId).startsWith('m') && remittances?.length > 0) ? remittances[0]._id : highlightId;
# ...
#  const { getRemittances... }
#  const [remittances, setRemittances] = useState([]);
# THIS IS THE REFERENCE ERROR!
# "ReferenceError: can't access lexical declaration 'remittances' before initialization" or something?
# Ah! Wait! The error is: "can't access lexical declaration 'p' before initialization"! No wait, what if the minifier renamed `remittances` to `p`?
# YES!! IN PRODUCTION BUILD, variable names are minified to `a`, `b`, `c`, `p`!!!
# The user might be testing on the built version or dev server minified it? No, dev server doesn't minify usually, but maybe it does!
# Or maybe `page` is minified to `p`? Or `remittances` is minified to `p`!
# The error "can't access lexical declaration 'p' before initialization" is exactly what you get when you access `remittances` before it's initialized on line 431, and the bundler minified `remittances` to `p`!

content = content.replace(
    "const effectiveHighlightId = (highlightId && String(highlightId).startsWith('m') && remittances?.length > 0) ? remittances[0]._id : highlightId;",
    "// effectiveHighlightId will be computed below"
)

old_state = """  const [remittances, setRemittances] = useState([]);"""
new_state = """  const [remittances, setRemittances] = useState([]);
  const effectiveHighlightId = (highlightId && String(highlightId).startsWith('m') && remittances?.length > 0) ? remittances[0]._id : highlightId;"""

content = content.replace(old_state, new_state)

with open('frontend/src/pages/admin/RemittanceMonitoringPage.jsx', 'w') as f:
    f.write(content)
