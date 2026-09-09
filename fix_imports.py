import re

with open("frontend/src/pages/SuperAdminDashboard.jsx", "r") as f:
    content = f.read()

bad_import = """}   ComposedChart,
  Line,
  Legend,
from "recharts";"""

good_import = """  ComposedChart,
  Line,
  Legend,
} from "recharts";"""

content = content.replace(bad_import, good_import)

with open("frontend/src/pages/SuperAdminDashboard.jsx", "w") as f:
    f.write(content)
