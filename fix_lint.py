import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

content = content.replace('import React, { useState } from "react";', 'import { useState } from "react";')
content = content.replace('  horizontalListSortingStrategy\n} from \'@dnd-kit/sortable\';', '} from \'@dnd-kit/sortable\';')

# Remove QuickActionCard definition
content = re.sub(r'const QuickActionCard =.*?\);\n', '', content, flags=re.DOTALL)

# formatNumber
content = content.replace('const SuperAdminDashboard = ({ dashboard, fleetHealth, formatCurrency, formatNumber }) => {', 'const SuperAdminDashboard = ({ dashboard, fleetHealth, formatCurrency }) => {')

# totalFleet
content = content.replace('const totalFleet = good + warn + crit + idle;\n', '')

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
