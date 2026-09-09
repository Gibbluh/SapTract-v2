const fs = require('fs');

let content = fs.readFileSync('frontend/src/pages/SuperAdminDashboard.jsx', 'utf8');

const mockDispatches = `
const MOCK_DISPATCHES = [
  { id: 1, name: "Juan Dela Cruz", vehicle: "NGQ 3326", route: "Cubao - Antipolo", avatar: "https://i.pravatar.cc/150?u=1" },
  { id: 2, name: "Pedro Penduko", vehicle: "UVP 9182", route: "Makati - BGC", avatar: "https://i.pravatar.cc/150?u=2" },
  { id: 3, name: "Cardo Dalisay", vehicle: "XYZ 1234", route: "Pasay - MOA", avatar: "https://i.pravatar.cc/150?u=3" },
  { id: 4, name: "Lito Lapid", vehicle: "DEF 5678", route: "Quezon Ave - UP", avatar: "https://i.pravatar.cc/150?u=4" }
];
`;

if (!content.includes('MOCK_DISPATCHES')) {
    content = content.replace('const mockRevenueData = [', mockDispatches + '\nconst mockRevenueData = [');
}

// wrap the right column
const rightColStart = `        {/* Right: Fleet Health Score */}`;
const rightColEnd = `          </Link>
        </div>`;

const wrappedCol = `        {/* Right Column */}
        <div className="flex flex-col gap-6">
          {/* Fleet Health Score */}
          <div className="bg-white border border-slate-200 rounded-3xl p-6 shadow-sm flex flex-col items-center">
`;

// It's a bit tricky to replace perfectly. Let's do it manually using Python script.
