import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

variables_to_insert = """
  // Safely extract from props
  const revenue = dashboard?.revenue || { total: 124567, trend: '+12.5%' };
  const totalRevenue = revenue.total;
  
  const fleetData = fleetHealth?.status || { good: 15, warning: 5, critical: 3, idle: 2 };
  const good = fleetData.good || 0;
  const warn = fleetData.warning || 0;
  const crit = fleetData.critical || 0;
  const idle = fleetData.idle || 0;
  const totalActive = good + warn + crit;
  
  const mockRevenueData = [
    { time: '6 AM', value: 12000 },
    { time: '9 AM', value: 35000 },
    { time: '12 PM', value: 48000 },
    { time: '3 PM', value: 72000 },
    { time: '6 PM', value: 95000 },
    { time: '9 PM', value: 110000 },
    { time: '12 AM', value: 124567 }
  ];

  const pieData = [
    { name: 'Good', value: good },
    { name: 'Warning', value: warn },
    { name: 'Critical', value: crit },
    { name: 'Idle', value: idle },
  ];
  const COLORS = ['#10b981', '#f59e0b', '#ef4444', '#94a3b8'];

  const MOCK_DISPATCHES = [
    { id: 1, name: "Juan Dela Cruz", vehicle: "NGQ 3326", route: "Cubao - Antipolo", avatar: "https://i.pravatar.cc/150?u=1" },
    { id: 2, name: "Pedro Penduko", vehicle: "UVP 9182", route: "Makati - BGC", avatar: "https://i.pravatar.cc/150?u=2" },
    { id: 3, name: "Cardo Dalisay", vehicle: "XYZ 1234", route: "Pasay - MOA", avatar: "https://i.pravatar.cc/150?u=3" },
    { id: 4, name: "Lito Lapid", vehicle: "DEF 5678", route: "Quezon Ave - UP", avatar: "https://i.pravatar.cc/150?u=4" }
  ];
"""

content = re.sub(r'const handleDragEnd = \(event\) => \{.*?\n  \};\n', r'\g<0>\n' + variables_to_insert, content, flags=re.DOTALL)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)

