import re

content = """import React, { useState, useMemo } from 'react';
import { 
  Search, Plus, Download, MoreVertical, X,
  Truck, CheckCircle, AlertTriangle, FileText, 
  Clock, Upload, Edit, Printer, ChevronRight,
  ChevronLeft, Check, Settings, LayoutGrid, List,
  QrCode, Activity, ShieldCheck, DownloadCloud, Image as ImageIcon,
  MoreHorizontal
} from 'lucide-react';

const MOCK_UNITS = [
  {
    id: "UNT-2024-001",
    plateNumber: "ABC-1234",
    bodyNumber: "101",
    make: "Toyota",
    model: "Hiace Commuter",
    year: "2022",
    type: "Van",
    capacity: 15,
    engineNo: "ENG123456789",
    chassisNo: "CHS987654321",
    color: "White",
    franchiseNo: "FR-2022-0001",
    ltfrbCaseNo: "2022-0001-A",
    regIssueDate: "2022-05-10",
    regExpiryDate: "2025-05-10",
    insuranceProvider: "Standard Insurance",
    insurancePolicyNo: "POL-998877",
    insuranceExpiryDate: "2024-10-15",
    dateAcquired: "2022-04-15",
    acquisitionCost: 1500000,
    route: "LANGGAM",
    status: "Available",
    healthScore: 92,
    documents: [
      { id: 1, type: "Registration", name: "OR_CR_ABC1234.pdf", date: "2022-05-10", size: "1.2MB" },
      { id: 2, type: "Insurance", name: "Insurance_Policy.pdf", date: "2023-10-10", size: "2.4MB" }
    ],
    avatar: "https://images.unsplash.com/photo-1621217346399-440263690d5f?auto=format&fit=crop&q=80&w=300"
  },
  {
    id: "UNT-2024-002",
    plateNumber: "XYZ-9876",
    bodyNumber: "102",
    make: "Mitsubishi",
    model: "L300",
    year: "2023",
    type: "Van",
    capacity: 17,
    engineNo: "ENG987654",
    chassisNo: "CHS123456",
    color: "Silver",
    franchiseNo: "FR-2023-0002",
    ltfrbCaseNo: "2023-0002-B",
    regIssueDate: "2023-01-20",
    regExpiryDate: "2026-01-20",
    insuranceProvider: "Pioneer Insurance",
    insurancePolicyNo: "POL-112233",
    insuranceExpiryDate: "2024-01-20", 
    dateAcquired: "2023-01-05",
    acquisitionCost: 1100000,
    route: "BAYAN-BAYANAN",
    status: "In Maintenance",
    healthScore: 55,
    documents: [],
    avatar: "https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?auto=format&fit=crop&q=80&w=300"
  },
  {
    id: "UNT-2024-003",
    plateNumber: "DEF-4567",
    bodyNumber: "103",
    make: "Toyota",
    model: "Coaster",
    year: "2020",
    type: "Mini Bus",
    capacity: 29,
    engineNo: "ENG456789",
    chassisNo: "CHS654321",
    color: "White/Blue",
    franchiseNo: "FR-2020-0003",
    ltfrbCaseNo: "2020-0003-C",
    regIssueDate: "2020-08-15",
    regExpiryDate: "2025-08-15",
    insuranceProvider: "Charter Ping An",
    insurancePolicyNo: "POL-445566",
    insuranceExpiryDate: "2024-12-01",
    dateAcquired: "2020-07-30",
    acquisitionCost: 2800000,
    route: "VILLAROSA",
    status: "Out of Service",
    healthScore: 25,
    documents: [],
    avatar: "https://images.unsplash.com/photo-1570125909232-eb263c188f7e?auto=format&fit=crop&q=80&w=300"
  }
];

for(let i=4; i<=25; i++) {
  MOCK_UNITS.push({
    id: `UNT-2024-00${i}`,
    plateNumber: `RND-${1000+i}`,
    bodyNumber: `${100+i}`,
    make: ["Toyota", "Isuzu", "Mitsubishi", "Hyundai"][i%4],
    model: ["Hiace", "QKR77", "L300", "H100"][i%4],
    year: "202" + (i%5),
    type: ["Van", "Modern PUV", "Jeepney", "Van"][i%4],
    capacity: 15 + (i%10),
    engineNo: `ENG${i}000`,
    chassisNo: `CHS${i}000`,
    color: ["White", "Silver", "Red", "Blue"][i%4],
    franchiseNo: `FR-2020-00${i}`,
    ltfrbCaseNo: `2020-00${i}-X`,
    regIssueDate: `2023-0${(i%9)+1}-10`,
    regExpiryDate: `2026-0${(i%9)+1}-10`,
    insuranceProvider: "Standard Insurance",
    insurancePolicyNo: `POL-00${i}`,
    insuranceExpiryDate: `2025-01-10`,
    dateAcquired: `2021-01-15`,
    acquisitionCost: 1500000 + (i*10000),
    route: ["LANGGAM", "VILLAROSA", "BAYAN-BAYANAN", "ESTRELLA", "CALAMBA", "UNASSIGNED"][i%6],
    status: ["Available", "In Maintenance", "Available", "Available"][i%4],
    healthScore: 40 + (i * 7) % 60,
    documents: [],
    avatar: i%3 === 0 ? "https://images.unsplash.com/photo-1554744512-d6c603f27c54?auto=format&fit=crop&q=80&w=300" : null
  });
}

const UnitManagementPage = () => {
  const [viewMode, setViewMode] = useState('grid');
  const [searchQuery, setSearchQuery] = useState('');
  const [statusFilter, setStatusFilter] = useState('All');
  const [selectedUnits, setSelectedUnits] = useState(new Set());
  
  const [drawerOpen, setDrawerOpen] = useState(false);
  const [selectedUnitData, setSelectedUnitData] = useState(null);
  const [drawerTab, setDrawerTab] = useState('Overview');
  
  const [formOpen, setFormOpen] = useState(false);
  
  const [page, setPage] = useState(1);
  const rowsPerPage = 12;
  const [unitsList] = useState(MOCK_UNITS);

  // --- Design System Helpers ---
  const getRouteBadgeStyles = (route) => {
    switch (route) {
      case 'LANGGAM': return 'bg-blue-100 text-blue-700 border-blue-200';
      case 'VILLAROSA': return 'bg-emerald-100 text-emerald-700 border-emerald-200';
      case 'BAYAN-BAYANAN': return 'bg-purple-100 text-purple-700 border-purple-200';
      case 'ESTRELLA': return 'bg-orange-100 text-orange-700 border-orange-200';
      case 'CALAMBA': return 'bg-red-100 text-red-700 border-red-200';
      default: return 'bg-gray-100 text-gray-700 border-gray-200';
    }
  };

  const getStatusConfig = (status) => {
    switch (status) {
      case 'Available': return { bg: 'bg-emerald-500', text: 'text-emerald-700', border: 'border-emerald-200', light: 'bg-emerald-50' };
      case 'In Maintenance': return { bg: 'bg-amber-500', text: 'text-amber-700', border: 'border-amber-200', light: 'bg-amber-50' };
      case 'Out of Service': return { bg: 'bg-red-500', text: 'text-red-700', border: 'border-red-200', light: 'bg-red-50' };
      default: return { bg: 'bg-gray-500', text: 'text-gray-700', border: 'border-gray-200', light: 'bg-gray-50' };
    }
  };

  const getHealthConfig = (score) => {
    if (score >= 80) return { color: 'bg-emerald-500', label: 'Good' };
    if (score >= 60) return { color: 'bg-amber-400', label: 'Fair' };
    if (score >= 40) return { color: 'bg-orange-500', label: 'Needs Attention' };
    return { color: 'bg-red-600', label: 'Critical' };
  };

  const getRegExpiryStatus = (expiryDate) => {
    const today = new Date();
    const expiry = new Date(expiryDate);
    const diffTime = expiry - today;
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    
    if (diffDays < 0) return { label: 'Expired', warning: true, icon: <AlertTriangle className="w-3 h-3 text-red-500" /> };
    if (diffDays <= 30) return { label: 'Expiring Soon', warning: true, icon: <Clock className="w-3 h-3 text-amber-500" /> };
    return { label: new Date(expiryDate).toLocaleDateString(), warning: false, icon: null };
  };

  // --- Derived Data ---
  const filteredUnits = useMemo(() => {
    return unitsList.filter(u => {
      if (statusFilter !== 'All' && u.status !== statusFilter) return false;
      const searchLower = searchQuery.toLowerCase();
      if (searchQuery && !(
        u.plateNumber.toLowerCase().includes(searchLower) ||
        u.bodyNumber.toLowerCase().includes(searchLower) ||
        `${u.make} ${u.model}`.toLowerCase().includes(searchLower)
      )) return false;
      return true;
    });
  }, [unitsList, statusFilter, searchQuery]);

  const paginatedUnits = filteredUnits.slice((page - 1) * rowsPerPage, page * rowsPerPage);
  const totalPages = Math.ceil(filteredUnits.length / rowsPerPage) || 1;

  // --- Actions ---
  const toggleSelection = (id, e) => {
    e.stopPropagation();
    const newSet = new Set(selectedUnits);
    if (newSet.has(id)) newSet.delete(id);
    else newSet.add(id);
    setSelectedUnits(newSet);
  };
  
  const toggleAll = () => {
    if (selectedUnits.size === paginatedUnits.length) {
      setSelectedUnits(new Set());
    } else {
      setSelectedUnits(new Set(paginatedUnits.map(u => u.id)));
    }
  };

  const openUnitDrawer = (unit) => {
    setSelectedUnitData(unit);
    setDrawerTab('Overview');
    setDrawerOpen(true);
  };

  return (
    <div className="flex flex-col h-full bg-gray-50 relative overflow-hidden">
      
      {/* HEADER BAR */}
      <header className="bg-white border-b border-gray-200 px-6 py-4 flex flex-col md:flex-row md:items-center justify-between gap-4 z-10 shrink-0 sticky top-0">
        <div className="flex items-center gap-3">
          <h1 className="text-2xl font-semibold text-gray-900">Units Management</h1>
          <span className="bg-blue-100 text-blue-700 text-xs font-bold px-2.5 py-1 rounded-full">{unitsList.length}</span>
        </div>
        
        <div className="flex flex-col sm:flex-row items-center gap-3 flex-1 justify-end">
          {/* Status Filter */}
          <div className="flex bg-gray-100 rounded-lg p-1">
            {['All', 'Available', 'In Maintenance', 'Out of Service'].map(status => (
              <button
                key={status}
                onClick={() => setStatusFilter(status)}
                className={`px-3 py-1.5 text-xs font-medium rounded-md transition-colors ${
                  statusFilter === status 
                    ? 'bg-white text-gray-900 shadow-sm' 
                    : 'text-gray-500 hover:text-gray-700'
                }`}
              >
                {status}
              </button>
            ))}
          </div>

          {/* Search */}
          <div className="relative">
            <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" />
            <input 
              type="text" 
              placeholder="Search plate, body..." 
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="pl-9 pr-4 py-2 border border-gray-300 rounded-lg text-sm w-full sm:w-64 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-shadow"
            />
          </div>

          {/* View Toggle */}
          <div className="flex bg-gray-100 rounded-lg p-1">
            <button
              title="Grid View"
              onClick={() => setViewMode('grid')}
              className={`p-1.5 rounded-md transition-colors ${viewMode === 'grid' ? 'bg-white text-blue-600 shadow-sm' : 'text-gray-500 hover:text-gray-700'}`}
            >
              <LayoutGrid className="w-4 h-4" />
            </button>
            <button
              title="Table View"
              onClick={() => setViewMode('table')}
              className={`p-1.5 rounded-md transition-colors ${viewMode === 'table' ? 'bg-white text-blue-600 shadow-sm' : 'text-gray-500 hover:text-gray-700'}`}
            >
              <List className="w-4 h-4" />
            </button>
          </div>

          {/* Add Unit */}
          <button 
            onClick={() => setFormOpen(true)}
            className="px-4 py-2 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700 transition-colors shadow-sm flex items-center gap-2 whitespace-nowrap"
          >
            <Plus className="w-4 h-4" /> Add Unit
          </button>
        </div>
      </header>

      {/* MAIN CONTENT */}
      <main className="flex-1 p-6 overflow-auto">
        
        {viewMode === 'grid' ? (
          /* CARD GRID VIEW */
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 pb-20">
            {paginatedUnits.map(unit => {
              const statusCfg = getStatusConfig(unit.status);
              const healthCfg = getHealthConfig(unit.healthScore);
              const isSelected = selectedUnits.has(unit.id);

              return (
                <div 
                  key={unit.id}
                  onClick={() => openUnitDrawer(unit)}
                  className={`group relative flex flex-col bg-white rounded-xl border transition-all duration-200 hover:-translate-y-1 hover:shadow-lg cursor-pointer overflow-hidden
                    ${isSelected ? 'border-blue-500 ring-1 ring-blue-500' : 'border-gray-200'}
                  `}
                >
                  {/* Selection Checkbox Layer */}
                  <div 
                    onClick={(e) => toggleSelection(unit.id, e)}
                    className={`absolute top-3 left-3 z-10 p-1.5 rounded-md transition-opacity 
                      ${isSelected ? 'opacity-100 bg-white/90 shadow-sm' : 'opacity-0 group-hover:opacity-100 bg-white/70 hover:bg-white'}
                    `}
                  >
                    <input 
                      type="checkbox" 
                      checked={isSelected}
                      readOnly
                      className="w-4 h-4 rounded border-gray-300 text-blue-600 focus:ring-blue-500 cursor-pointer"
                    />
                  </div>

                  {/* Photo Header */}
                  <div className="relative h-40 bg-gray-100 flex items-center justify-center overflow-hidden shrink-0">
                    {unit.avatar ? (
                      <img src={unit.avatar} alt={unit.plateNumber} className="w-full h-full object-cover" />
                    ) : (
                      <Truck className="w-12 h-12 text-gray-300" />
                    )}
                    {/* Status Overlay */}
                    <div className="absolute top-3 right-3 flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-white/90 backdrop-blur-sm shadow-sm border border-white/20">
                      <div className={`w-2 h-2 rounded-full ${statusCfg.bg}`}></div>
                      <span className="text-[10px] font-bold text-gray-800 uppercase tracking-wide">{unit.status}</span>
                    </div>
                  </div>

                  {/* Card Body */}
                  <div className="p-4 flex flex-col flex-1">
                    <div className="flex justify-between items-start mb-2">
                      <div>
                        <h3 className="text-lg font-bold text-gray-900 font-mono tracking-tight">{unit.plateNumber}</h3>
                        <p className="text-xs text-gray-500 font-medium">Body: <span className="text-gray-900">{unit.bodyNumber}</span></p>
                      </div>
                      <div className={`px-2 py-0.5 rounded text-[10px] font-bold uppercase tracking-wider border ${getRouteBadgeStyles(unit.route)}`}>
                        {unit.route}
                      </div>
                    </div>
                    
                    <p className="text-xs text-gray-600 mb-4">{unit.make} {unit.model} {unit.year}</p>

                    <div className="mt-auto pt-4 border-t border-gray-100 space-y-1">
                      <div className="flex justify-between text-[10px] font-medium text-gray-500 mb-1">
                        <span>Health Score</span>
                        <span>{unit.healthScore}%</span>
                      </div>
                      <div className="h-1.5 w-full bg-gray-100 rounded-full overflow-hidden">
                        <div className={`h-full rounded-full ${healthCfg.color}`} style={{ width: `${unit.healthScore}%` }}></div>
                      </div>
                    </div>
                  </div>

                  {/* Quick Actions (Hover) */}
                  <div className="absolute bottom-16 right-4 flex flex-col gap-2 opacity-0 group-hover:opacity-100 transition-opacity translate-x-2 group-hover:translate-x-0">
                    <button onClick={(e) => { e.stopPropagation(); }} className="p-2 bg-white rounded-full shadow-md text-gray-500 hover:text-blue-600 hover:bg-blue-50 transition-colors" title="Print QR">
                      <QrCode className="w-4 h-4" />
                    </button>
                    <button onClick={(e) => { e.stopPropagation(); }} className="p-2 bg-white rounded-full shadow-md text-gray-500 hover:text-blue-600 hover:bg-blue-50 transition-colors" title="Edit">
                      <Edit className="w-4 h-4" />
                    </button>
                  </div>
                </div>
              );
            })}
          </div>
        ) : (
          /* COMPACT TABLE VIEW */
          <div className="bg-white rounded-xl border border-gray-200 shadow-sm overflow-hidden pb-20">
            <div className="overflow-x-auto">
              <table className="w-full text-left text-sm">
                <thead>
                  <tr className="bg-gray-50 border-b border-gray-200 text-xs font-semibold text-gray-600 uppercase tracking-wider">
                    <th className="px-4 py-3 w-10">
                      <input 
                        type="checkbox" 
                        className="rounded border-gray-300 text-blue-600 focus:ring-blue-500 cursor-pointer"
                        checked={selectedUnits.size === paginatedUnits.length && paginatedUnits.length > 0}
                        onChange={toggleAll}
                      />
                    </th>
                    <th className="px-4 py-3">Unit</th>
                    <th className="px-4 py-3">Status</th>
                    <th className="px-4 py-3">Vehicle Details</th>
                    <th className="px-4 py-3">Route</th>
                    <th className="px-4 py-3">Reg. Expiry</th>
                    <th className="px-4 py-3">Health Score</th>
                    <th className="px-4 py-3 text-right">Actions</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-gray-100">
                  {paginatedUnits.map(unit => {
                    const statusCfg = getStatusConfig(unit.status);
                    const healthCfg = getHealthConfig(unit.healthScore);
                    const regStatus = getRegExpiryStatus(unit.regExpiryDate);
                    const isSelected = selectedUnits.has(unit.id);

                    return (
                      <tr 
                        key={unit.id}
                        onClick={() => openUnitDrawer(unit)}
                        className={`hover:bg-gray-50 transition-colors cursor-pointer ${isSelected ? 'bg-blue-50/30' : ''}`}
                      >
                        <td className="px-4 py-3" onClick={(e) => toggleSelection(unit.id, e)}>
                          <input 
                            type="checkbox" 
                            checked={isSelected}
                            readOnly
                            className="rounded border-gray-300 text-blue-600 focus:ring-blue-500 cursor-pointer"
                          />
                        </td>
                        <td className="px-4 py-3">
                          <div className="flex items-center gap-3">
                            <div className="w-10 h-10 rounded-lg overflow-hidden bg-gray-100 border border-gray-200 shrink-0 flex items-center justify-center">
                              {unit.avatar ? (
                                <img src={unit.avatar} alt="avatar" className="w-full h-full object-cover" />
                              ) : (
                                <Truck className="w-5 h-5 text-gray-400" />
                              )}
                            </div>
                            <div>
                              <div className="font-mono font-bold text-gray-900 tracking-tight">{unit.plateNumber}</div>
                              <div className="text-xs text-gray-500">Body: {unit.bodyNumber}</div>
                            </div>
                          </div>
                        </td>
                        <td className="px-4 py-3">
                          <div className={`inline-flex items-center gap-1.5 px-2 py-1 rounded-full ${statusCfg.light} ${statusCfg.text} border ${statusCfg.border}`}>
                            <div className={`w-1.5 h-1.5 rounded-full ${statusCfg.bg}`}></div>
                            <span className="text-[10px] font-bold uppercase tracking-wider">{unit.status}</span>
                          </div>
                        </td>
                        <td className="px-4 py-3">
                          <div className="font-medium text-gray-900">{unit.make} {unit.model}</div>
                          <div className="text-xs text-gray-500">{unit.year} • {unit.type}</div>
                        </td>
                        <td className="px-4 py-3">
                          <div className={`inline-flex px-2 py-0.5 rounded text-[10px] font-bold uppercase tracking-wider border ${getRouteBadgeStyles(unit.route)}`}>
                            {unit.route}
                          </div>
                        </td>
                        <td className="px-4 py-3">
                          <div className="flex items-center gap-2">
                            <span className={`text-xs font-medium ${regStatus.warning ? 'text-amber-600' : 'text-gray-700'}`}>
                              {regStatus.label}
                            </span>
                            {regStatus.icon}
                          </div>
                        </td>
                        <td className="px-4 py-3">
                          <div className="w-24">
                            <div className="flex justify-between text-[10px] font-medium text-gray-500 mb-1">
                              <span>{unit.healthScore}%</span>
                            </div>
                            <div className="h-1.5 w-full bg-gray-100 rounded-full overflow-hidden">
                              <div className={`h-full rounded-full ${healthCfg.color}`} style={{ width: `${unit.healthScore}%` }}></div>
                            </div>
                          </div>
                        </td>
                        <td className="px-4 py-3 text-right">
                          <button onClick={(e) => e.stopPropagation()} className="p-1.5 text-gray-400 hover:text-blue-600 hover:bg-blue-50 rounded transition-colors">
                            <MoreHorizontal className="w-4 h-4" />
                          </button>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </div>
        )}

        {/* PAGINATION */}
        <div className="flex items-center justify-between mt-6">
          <p className="text-sm text-gray-500">
            Showing <span className="font-medium">{filteredUnits.length > 0 ? (page - 1) * rowsPerPage + 1 : 0}</span> to <span className="font-medium">{Math.min(page * rowsPerPage, filteredUnits.length)}</span> of <span className="font-medium">{filteredUnits.length}</span> results
          </p>
          <div className="flex gap-2">
            <button 
              onClick={() => setPage(p => Math.max(1, p - 1))}
              disabled={page === 1}
              className="p-2 border border-gray-200 rounded-lg bg-white text-gray-500 hover:bg-gray-50 disabled:opacity-50 transition-colors"
            >
              <ChevronLeft className="w-4 h-4" />
            </button>
            <button 
              onClick={() => setPage(p => Math.min(totalPages, p + 1))}
              disabled={page === totalPages || totalPages === 0}
              className="p-2 border border-gray-200 rounded-lg bg-white text-gray-500 hover:bg-gray-50 disabled:opacity-50 transition-colors"
            >
              <ChevronRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      </main>

      {/* BULK ACTION BAR */}
      {selectedUnits.size > 0 && (
        <div className="absolute bottom-6 left-1/2 -translate-x-1/2 z-30 bg-gray-900 text-white px-6 py-3 rounded-xl shadow-2xl flex items-center gap-6 animate-in slide-in-from-bottom-8">
          <span className="font-semibold text-sm whitespace-nowrap">{selectedUnits.size} selected</span>
          <div className="h-5 w-px bg-gray-700"></div>
          <button className="text-sm font-medium hover:text-blue-400 transition-colors flex items-center gap-2">
            <Activity className="w-4 h-4" /> Change Status
          </button>
          <button className="text-sm font-medium hover:text-blue-400 transition-colors flex items-center gap-2">
            <DownloadCloud className="w-4 h-4" /> Download QRs
          </button>
          <div className="h-5 w-px bg-gray-700"></div>
          <button onClick={() => setSelectedUnits(new Set())} className="p-1 hover:bg-gray-800 rounded transition-colors text-gray-400 hover:text-white">
            <X className="w-4 h-4" />
          </button>
        </div>
      )}

      {/* DETAIL DRAWER */}
      {drawerOpen && selectedUnitData && (
        <div className="absolute inset-0 z-50 flex justify-end">
          <div className="absolute inset-0 bg-gray-900/20 backdrop-blur-sm" onClick={() => setDrawerOpen(false)}></div>
          <div className="w-full max-w-2xl bg-gray-50 h-full flex flex-col relative animate-in slide-in-from-right overflow-hidden shadow-2xl">
            
            {/* Drawer Hero Header */}
            <div className="relative h-48 bg-gray-800 shrink-0">
              {selectedUnitData.avatar ? (
                <img src={selectedUnitData.avatar} alt="Unit" className="w-full h-full object-cover opacity-70" />
              ) : (
                <div className="w-full h-full flex items-center justify-center opacity-70">
                  <Truck className="w-20 h-20 text-gray-500" />
                </div>
              )}
              
              <div className="absolute inset-0 bg-gradient-to-t from-gray-900/90 to-transparent"></div>
              
              <button 
                onClick={() => setDrawerOpen(false)} 
                className="absolute top-4 right-4 p-2 bg-black/20 hover:bg-black/40 text-white rounded-full backdrop-blur-md transition-colors"
              >
                <X className="w-5 h-5" />
              </button>

              <div className="absolute bottom-4 left-6 right-6 flex items-end justify-between">
                <div>
                  <div className="flex items-center gap-2 mb-2">
                    <span className={`px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider ${getStatusConfig(selectedUnitData.status).bg} text-white`}>
                      {selectedUnitData.status}
                    </span>
                    <span className={`px-2 py-0.5 rounded text-[10px] font-bold uppercase tracking-wider border bg-black/40 border-white/20 text-white backdrop-blur-md`}>
                      {selectedUnitData.route}
                    </span>
                  </div>
                  <h2 className="text-3xl font-bold font-mono text-white tracking-tight">{selectedUnitData.plateNumber}</h2>
                  <p className="text-gray-300 text-sm">Body No: {selectedUnitData.bodyNumber} • {selectedUnitData.make} {selectedUnitData.model}</p>
                </div>
                <div className="flex gap-2">
                  <button className="p-2 bg-white/10 hover:bg-white/20 text-white rounded-lg backdrop-blur-md transition-colors border border-white/10" title="Print QR">
                    <QrCode className="w-4 h-4" />
                  </button>
                  <button className="p-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg transition-colors shadow-lg" title="Edit">
                    <Edit className="w-4 h-4" />
                  </button>
                </div>
              </div>
            </div>

            {/* Drawer Tabs */}
            <div className="flex px-6 bg-white border-b border-gray-200 shrink-0">
              {['Overview', 'Documents', 'Health & Status', 'Activity Log'].map(tab => (
                <button
                  key={tab}
                  onClick={() => setDrawerTab(tab)}
                  className={`px-4 py-3.5 text-sm font-medium border-b-2 transition-colors -mb-px ${
                    drawerTab === tab 
                      ? 'border-blue-600 text-blue-600' 
                      : 'border-transparent text-gray-500 hover:text-gray-800'
                  }`}
                >
                  {tab}
                </button>
              ))}
            </div>

            {/* Drawer Content Area */}
            <div className="flex-1 overflow-y-auto p-6 space-y-6">
              
              {drawerTab === 'Overview' && (
                <>
                  <div className="grid grid-cols-2 gap-4">
                    <div className="bg-white p-4 rounded-xl border border-gray-200 shadow-sm">
                      <h3 className="text-xs font-bold text-gray-400 uppercase tracking-wider mb-4">Vehicle Details</h3>
                      <div className="space-y-3">
                        <div><p className="text-xs text-gray-500">Make & Model</p><p className="font-medium text-gray-900">{selectedUnitData.make} {selectedUnitData.model}</p></div>
                        <div><p className="text-xs text-gray-500">Year</p><p className="font-medium text-gray-900">{selectedUnitData.year}</p></div>
                        <div><p className="text-xs text-gray-500">Type / Capacity</p><p className="font-medium text-gray-900">{selectedUnitData.type} • {selectedUnitData.capacity} pax</p></div>
                        <div><p className="text-xs text-gray-500">Engine / Chassis</p><p className="font-mono text-xs text-gray-900 mt-0.5">{selectedUnitData.engineNo} <br/> {selectedUnitData.chassisNo}</p></div>
                      </div>
                    </div>

                    <div className="bg-white p-4 rounded-xl border border-gray-200 shadow-sm">
                      <h3 className="text-xs font-bold text-gray-400 uppercase tracking-wider mb-4">Registration & Legal</h3>
                      <div className="space-y-3">
                        <div><p className="text-xs text-gray-500">Franchise No.</p><p className="font-medium text-gray-900">{selectedUnitData.franchiseNo}</p></div>
                        <div><p className="text-xs text-gray-500">LTFRB Case No.</p><p className="font-medium text-gray-900">{selectedUnitData.ltfrbCaseNo}</p></div>
                        <div>
                          <p className="text-xs text-gray-500">Registration Expiry</p>
                          <div className="flex items-center gap-2 mt-0.5">
                            <p className="font-medium text-gray-900">{new Date(selectedUnitData.regExpiryDate).toLocaleDateString()}</p>
                            {getRegExpiryStatus(selectedUnitData.regExpiryDate).warning && (
                              <AlertTriangle className="w-3.5 h-3.5 text-amber-500" />
                            )}
                          </div>
                        </div>
                        <div><p className="text-xs text-gray-500">Acquisition</p><p className="font-medium text-gray-900">{new Date(selectedUnitData.dateAcquired).toLocaleDateString()} • ₱{selectedUnitData.acquisitionCost.toLocaleString()}</p></div>
                      </div>
                    </div>
                  </div>

                  <div className="bg-white p-4 rounded-xl border border-gray-200 shadow-sm">
                    <h3 className="text-xs font-bold text-gray-400 uppercase tracking-wider mb-4">Insurance Details</h3>
                    <div className="grid grid-cols-3 gap-4">
                      <div><p className="text-xs text-gray-500">Provider</p><p className="font-medium text-gray-900">{selectedUnitData.insuranceProvider}</p></div>
                      <div><p className="text-xs text-gray-500">Policy No.</p><p className="font-medium text-gray-900">{selectedUnitData.insurancePolicyNo}</p></div>
                      <div><p className="text-xs text-gray-500">Expiry Date</p><p className="font-medium text-gray-900">{new Date(selectedUnitData.insuranceExpiryDate).toLocaleDateString()}</p></div>
                    </div>
                  </div>
                </>
              )}

              {drawerTab === 'Documents' && (
                <div className="space-y-4">
                  <div className="flex justify-between items-center">
                    <h3 className="text-sm font-bold text-gray-900">Digital Files</h3>
                    <button className="text-sm text-blue-600 font-medium hover:text-blue-700 flex items-center gap-1">
                      <Plus className="w-4 h-4" /> Upload
                    </button>
                  </div>
                  
                  {selectedUnitData.documents.length > 0 ? (
                    <div className="grid grid-cols-2 gap-4">
                      {selectedUnitData.documents.map(doc => (
                        <div key={doc.id} className="border border-gray-200 rounded-xl p-4 flex gap-3 bg-white hover:border-blue-300 transition-colors cursor-pointer group">
                          <div className="w-10 h-10 rounded-lg bg-red-50 text-red-600 flex items-center justify-center shrink-0">
                            <FileText className="w-5 h-5" />
                          </div>
                          <div className="overflow-hidden flex-1">
                            <p className="font-medium text-sm text-gray-900 truncate">{doc.name}</p>
                            <div className="flex items-center gap-2 mt-1">
                              <span className="text-[10px] font-semibold uppercase tracking-wider text-gray-500 bg-gray-100 px-1.5 rounded">{doc.type}</span>
                              <span className="text-xs text-gray-400">{doc.size}</span>
                            </div>
                          </div>
                        </div>
                      ))}
                    </div>
                  ) : (
                    <div className="border-2 border-dashed border-gray-200 rounded-xl p-8 text-center bg-gray-50">
                      <div className="w-12 h-12 bg-white rounded-full flex items-center justify-center mx-auto mb-3 shadow-sm border border-gray-100">
                        <Upload className="w-5 h-5 text-gray-400" />
                      </div>
                      <p className="font-medium text-gray-900">No documents found</p>
                      <p className="text-xs text-gray-500 mt-1">Drag and drop files here, or click to browse.</p>
                    </div>
                  )}
                </div>
              )}

              {drawerTab === 'Health & Status' && (
                <div className="space-y-6">
                  {/* Health Score Summary */}
                  <div className="bg-white p-5 rounded-xl border border-gray-200 shadow-sm flex items-center gap-6">
                    <div className="relative w-24 h-24 shrink-0 flex items-center justify-center">
                      <svg className="w-full h-full transform -rotate-90" viewBox="0 0 36 36">
                        <path className="text-gray-100" strokeWidth="3" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                        <path className={getHealthConfig(selectedUnitData.healthScore).color.replace('bg-', 'text-')} strokeDasharray={`${selectedUnitData.healthScore}, 100`} strokeWidth="3" strokeLinecap="round" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                      </svg>
                      <div className="absolute flex flex-col items-center justify-center">
                        <span className="text-2xl font-bold text-gray-900">{selectedUnitData.healthScore}</span>
                      </div>
                    </div>
                    <div>
                      <h3 className="text-lg font-bold text-gray-900 mb-1">Fleet Health Score</h3>
                      <p className="text-sm text-gray-500 mb-3">Based on recent maintenance, mileage, and active alerts.</p>
                      <span className={`inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-bold uppercase tracking-wider ${getHealthConfig(selectedUnitData.healthScore).color} text-white`}>
                        <ShieldCheck className="w-3.5 h-3.5" /> {getHealthConfig(selectedUnitData.healthScore).label}
                      </span>
                    </div>
                  </div>

                  <div className="flex items-center justify-between">
                    <h3 className="text-sm font-bold text-gray-900 flex items-center gap-2"><Settings className="w-4 h-4 text-blue-600"/> Recent Maintenance</h3>
                    <button className="text-sm text-blue-600 font-medium hover:text-blue-700">View All</button>
                  </div>
                  <div className="bg-white rounded-xl border border-gray-200 shadow-sm overflow-hidden">
                    <table className="w-full text-left">
                      <tbody className="divide-y divide-gray-100 text-sm">
                        <tr className="hover:bg-gray-50">
                          <td className="px-4 py-3 text-gray-500 whitespace-nowrap text-xs">Oct 12, 2024</td>
                          <td className="px-4 py-3 font-medium text-gray-900">Preventive</td>
                          <td className="px-4 py-3 text-gray-600">Oil change and brake pad replacement</td>
                        </tr>
                        <tr className="hover:bg-gray-50">
                          <td className="px-4 py-3 text-gray-500 whitespace-nowrap text-xs">Sep 05, 2024</td>
                          <td className="px-4 py-3 font-medium text-gray-900">Repair</td>
                          <td className="px-4 py-3 text-gray-600">Aircon cleaning and freon refill</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              )}

              {drawerTab === 'Activity Log' && (
                <div className="space-y-4">
                  <div className="relative border-l-2 border-gray-200 ml-3 space-y-6 pb-4">
                    <div className="relative">
                      <div className="absolute -left-[21px] bg-blue-100 rounded-full p-1.5 border border-white">
                        <Activity className="w-3 h-3 text-blue-600" />
                      </div>
                      <div className="pl-6">
                        <p className="text-sm font-medium text-gray-900">Status changed to <span className="font-bold">Available</span></p>
                        <p className="text-xs text-gray-500 mt-0.5">By Super Admin • Today, 10:45 AM</p>
                      </div>
                    </div>
                    <div className="relative">
                      <div className="absolute -left-[21px] bg-gray-100 rounded-full p-1.5 border border-white">
                        <Edit className="w-3 h-3 text-gray-600" />
                      </div>
                      <div className="pl-6">
                        <p className="text-sm font-medium text-gray-900">Route reassigned to <span className="font-bold">{selectedUnitData.route}</span></p>
                        <p className="text-xs text-gray-500 mt-0.5">By Dispatcher • Yesterday, 2:30 PM</p>
                      </div>
                    </div>
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      )}

      {/* Basic Form Modal placeholder */}
      {formOpen && (
        <div className="absolute inset-0 z-50 flex items-center justify-center p-4">
          <div className="absolute inset-0 bg-gray-900/40 backdrop-blur-sm" onClick={() => setFormOpen(false)}></div>
          <div className="bg-white rounded-2xl w-full max-w-3xl max-h-[90vh] flex flex-col relative shadow-2xl animate-in fade-in zoom-in-95">
            <div className="p-6 border-b border-gray-100 flex items-center justify-between shrink-0">
              <h2 className="text-xl font-bold text-gray-900">Add New Unit</h2>
              <button onClick={() => setFormOpen(false)} className="p-2 hover:bg-gray-100 rounded-full transition-colors text-gray-500"><X className="w-5 h-5"/></button>
            </div>
            <div className="p-6 overflow-y-auto flex-1">
               <div className="text-center py-12 text-gray-500">
                  <ImageIcon className="w-12 h-12 mx-auto text-gray-300 mb-3" />
                  <p>Form implementation matching modern standards goes here.</p>
               </div>
            </div>
            <div className="p-4 border-t border-gray-100 bg-gray-50 flex justify-end gap-3 rounded-b-2xl shrink-0">
              <button onClick={() => setFormOpen(false)} className="px-4 py-2 font-medium text-gray-600 hover:text-gray-900 transition-colors">Cancel</button>
              <button className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg shadow-sm transition-colors">Save Unit</button>
            </div>
          </div>
        </div>
      )}

    </div>
  );
};

export default UnitManagementPage;
"""

with open('frontend/src/pages/admin/UnitManagementPage.jsx', 'w') as f:
    f.write(content)
