import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

new_content = """import React, { useState } from "react";
import {
  DndContext,
  closestCenter,
  KeyboardSensor,
  PointerSensor,
  useSensor,
  useSensors,
} from '@dnd-kit/core';
import {
  arrayMove,
  SortableContext,
  sortableKeyboardCoordinates,
  rectSortingStrategy,
} from '@dnd-kit/sortable';
import { useSortable } from '@dnd-kit/sortable';
import { CSS } from '@dnd-kit/utilities';
import {
  TrendingUp,
  Truck,
  ClipboardList,
  Users,
  ShieldAlert,
  Fuel,
  Activity,
  ArrowUpRight,
  Info
} from "lucide-react";
import { Link } from "react-router-dom";
import {
  AreaChart,
  Area,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell
} from "recharts";

const WIDGET_CLASSES = {
  'metric-revenue': 'col-span-12 sm:col-span-6 xl:col-span-3 2xl:col-span-2 h-full flex',
  'metric-active': 'col-span-12 sm:col-span-6 xl:col-span-3 2xl:col-span-2 h-full flex',
  'metric-pending': 'col-span-12 sm:col-span-6 xl:col-span-2 h-full flex',
  'metric-users': 'col-span-12 sm:col-span-6 xl:col-span-2 h-full flex',
  'metric-alerts': 'col-span-12 sm:col-span-6 xl:col-span-2 h-full flex',
  'chart-revenue': 'col-span-12 lg:col-span-8 flex h-full',
  'chart-fleet': 'col-span-12 lg:col-span-4 flex h-full',
  'chart-dispatches': 'col-span-12 lg:col-span-4 flex h-full'
};

const SortableItem = ({ id, children, className }) => {
  const {
    attributes,
    listeners,
    setNodeRef,
    transform,
    transition,
    isDragging,
  } = useSortable({ id });

  const style = {
    transform: CSS.Transform.toString(transform),
    transition,
    zIndex: isDragging ? 50 : 1,
    opacity: isDragging ? 0.8 : 1,
  };

  return (
    <div ref={setNodeRef} style={style} className={`relative group ${className || ''}`} {...attributes} {...listeners}>
      {children}
    </div>
  );
};

const SuperAdminDashboard = ({ dashboard, fleetHealth, formatCurrency }) => {
  const [timeFilter, setTimeFilter] = useState('Today');
  const [widgetOrder, setWidgetOrder] = useState([
    'metric-revenue', 'metric-active', 'metric-pending', 'metric-users', 'metric-alerts',
    'chart-revenue', 'chart-fleet', 'chart-dispatches'
  ]);

  const sensors = useSensors(
    useSensor(PointerSensor, { activationConstraint: { distance: 5 } }),
    useSensor(KeyboardSensor, { coordinateGetter: sortableKeyboardCoordinates })
  );

  const handleDragEnd = (event) => {
    const { active, over } = event;
    if (!over) return;
    if (active.id !== over.id) {
      setWidgetOrder((items) => {
        const oldIndex = items.indexOf(active.id);
        const newIndex = items.indexOf(over.id);
        return arrayMove(items, oldIndex, newIndex);
      });
    }
  };

  // Safe mock multiplication factor based on time filter
  const tfMult = timeFilter === '30 Days' ? 30 : timeFilter === '7 Days' ? 7 : 1;

  const revenue = dashboard?.revenue || { total: 124567, trend: '+12.5%' };
  const totalRevenue = (revenue.total || 124567) * tfMult;
  
  const fleetData = fleetHealth?.status || { good: 15, warning: 5, critical: 3, idle: 2 };
  const good = fleetData.good || 0;
  const warn = fleetData.warning || 0;
  const crit = fleetData.critical || 0;
  const idle = fleetData.idle || 0;
  const totalActive = good + warn + crit;
  
  const mockRevenueData = [
    { time: '6 AM', value: 12000 * tfMult },
    { time: '9 AM', value: 35000 * tfMult },
    { time: '12 PM', value: 48000 * tfMult },
    { time: '3 PM', value: 72000 * tfMult },
    { time: '6 PM', value: 95000 * tfMult },
    { time: '9 PM', value: 110000 * tfMult },
    { time: '12 AM', value: 124567 * tfMult }
  ];

  const pieData = [
    { name: 'Good', value: good },
    { name: 'Warning', value: warn },
    { name: 'Critical', value: crit },
    { name: 'Idle', value: idle },
  ];
  const COLORS = ['#10b981', '#f59e0b', '#ef4444', '#94a3b8'];

  // Calculate current date strings
  const todayDate = new Date();
  const dateStr = todayDate.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });

  const MOCK_DISPATCHES = [
    { id: 1, name: "Juan Dela Cruz", vehicle: "NGQ 3326", route: "Cubao - Antipolo", avatar: "https://i.pravatar.cc/150?u=1", schedule: "06:00 AM - 02:00 PM" },
    { id: 2, name: "Pedro Penduko", vehicle: "UVP 9182", route: "Makati - BGC", avatar: "https://i.pravatar.cc/150?u=2", schedule: "08:00 AM - 04:00 PM" },
    { id: 3, name: "Cardo Dalisay", vehicle: "XYZ 1234", route: "Pasay - MOA", avatar: "https://i.pravatar.cc/150?u=3", schedule: "10:00 AM - 06:00 PM" },
    { id: 4, name: "Lito Lapid", vehicle: "DEF 5678", route: "Quezon Ave - UP", avatar: "https://i.pravatar.cc/150?u=4", schedule: "02:00 PM - 10:00 PM" }
  ];

  const widgets = {
    'metric-revenue': (
      <SortableItem id="metric-revenue" key="metric-revenue" className={WIDGET_CLASSES['metric-revenue']}>
        <div className="dark:bg-slate-800 bg-white border dark:border-slate-700 border-slate-200 rounded-2xl p-5 shadow-sm relative overflow-hidden flex flex-col w-full h-full cursor-grab active:cursor-grabbing">
          <div className="flex justify-between items-start mb-2">
            <div className="w-10 h-10 dark:bg-blue-900/50 bg-blue-50 rounded-lg flex items-center justify-center">
              <TrendingUp className="dark:text-blue-400 text-blue-600 w-5 h-5" />
            </div>
            <div className="dark:bg-emerald-900/50 bg-emerald-100 dark:text-emerald-400 text-emerald-700 text-[10px] font-bold px-2 py-1 rounded-full flex items-center">
              <ArrowUpRight className="w-3 h-3 mr-1" />
              +12.5%
            </div>
          </div>
          <div className="mt-2">
            <p className="text-xs font-medium dark:text-slate-400 text-slate-500 mb-1">Total Revenue {timeFilter}</p>
            <h2 className="text-2xl sm:text-3xl font-black dark:text-white text-slate-900 tracking-tight">
              {formatCurrency ? formatCurrency(totalRevenue) : `₱${totalRevenue.toLocaleString()}`}
            </h2>
          </div>
          <div className="mt-auto pt-4 flex justify-between items-end">
            <p className="text-[11px] dark:text-slate-500 text-slate-400">vs ₱{(110800 * tfMult).toLocaleString()} previous</p>
            <div className="flex items-end gap-1 opacity-80">
              <div className="w-2 dark:bg-blue-800 bg-blue-200 rounded-sm h-3"></div>
              <div className="w-2 dark:bg-blue-700 bg-blue-300 rounded-sm h-4"></div>
              <div className="w-2 dark:bg-blue-600 bg-blue-400 rounded-sm h-5"></div>
              <div className="w-2 dark:bg-blue-500 bg-blue-500 rounded-sm h-7"></div>
              <div className="w-2 dark:bg-blue-400 bg-blue-600 rounded-sm h-8"></div>
            </div>
          </div>
        </div>
      </SortableItem>
    ),
    'metric-active': (
      <SortableItem id="metric-active" key="metric-active" className={WIDGET_CLASSES['metric-active']}>
        <div className="dark:bg-slate-800 bg-white border dark:border-slate-700 border-slate-200 rounded-2xl p-5 shadow-sm flex flex-col w-full h-full cursor-grab active:cursor-grabbing">
          <div className="flex justify-between items-start mb-2">
            <div className="w-10 h-10 dark:bg-emerald-900/50 bg-emerald-50 rounded-lg flex items-center justify-center">
              <Truck className="dark:text-emerald-400 text-emerald-600 w-5 h-5" />
            </div>
            <div className="dark:bg-emerald-900/50 bg-emerald-100 dark:text-emerald-400 text-emerald-700 text-[10px] font-bold px-2 py-1 rounded-full">
              72% Utilization
            </div>
          </div>
          <div className="mt-2">
            <p className="text-xs font-medium dark:text-slate-400 text-slate-500 mb-1">Active Fleet</p>
            <h2 className="text-2xl sm:text-3xl font-black dark:text-white text-slate-900 tracking-tight flex items-baseline">
              {totalActive} <span className="text-sm font-medium dark:text-slate-500 text-slate-400 ml-1">/25 Units</span>
            </h2>
          </div>
          <div className="mt-auto pt-4">
            <div className="w-full h-2 rounded-full overflow-hidden flex mb-2">
              <div className="bg-emerald-500 h-full" style={{ width: '60%' }}></div>
              <div className="bg-amber-400 h-full" style={{ width: '25%' }}></div>
              <div className="bg-red-500 h-full" style={{ width: '15%' }}></div>
            </div>
            <div className="flex justify-between items-center text-[10px]">
              <div className="flex items-center gap-3">
                <span className="flex items-center dark:text-slate-400 text-slate-500"><span className="w-2 h-2 rounded-full bg-emerald-500 mr-1"></span> {good} Good</span>
                <span className="flex items-center dark:text-slate-400 text-slate-500"><span className="w-2 h-2 rounded-full bg-amber-400 mr-1"></span> {warn} Warn</span>
              </div>
              <Link to="/units" className="dark:text-emerald-400 text-emerald-600 font-semibold hover:underline relative z-20" onClick={(e) => e.stopPropagation()}>View</Link>
            </div>
          </div>
        </div>
      </SortableItem>
    ),
    'metric-pending': (
      <SortableItem id="metric-pending" key="metric-pending" className={WIDGET_CLASSES['metric-pending']}>
        <div className="dark:bg-slate-800 bg-white border dark:border-slate-700 border-slate-200 rounded-2xl p-5 shadow-sm flex flex-col w-full h-full cursor-grab active:cursor-grabbing">
          <div className="flex justify-between items-start mb-2">
            <div className="w-10 h-10 dark:bg-amber-900/50 bg-amber-50 rounded-lg flex items-center justify-center">
              <ClipboardList className="dark:text-amber-400 text-amber-500 w-5 h-5" />
            </div>
            <div className="dark:bg-amber-900/50 bg-amber-100 dark:text-amber-400 text-amber-700 text-[10px] font-bold px-2 py-1 rounded-full flex items-center">
              <span className="w-1.5 h-1.5 rounded-full bg-amber-500 mr-1"></span>
              Urgent
            </div>
          </div>
          <div className="mt-2">
            <p className="text-xs font-medium dark:text-slate-400 text-slate-500 mb-1">Pending Actions</p>
            <h2 className="text-2xl sm:text-3xl font-black dark:text-white text-slate-900 tracking-tight flex items-baseline">
              {12 * tfMult} <span className="text-sm font-medium dark:text-slate-500 text-slate-400 ml-1">tasks</span>
            </h2>
          </div>
          <div className="mt-auto pt-5 flex justify-between items-center">
            <p className="text-[11px] dark:text-slate-500 text-slate-500">{4 * tfMult} fuel • {5 * tfMult} shift • {3 * tfMult} maint</p>
            <button className="dark:text-amber-400 text-amber-600 text-xs font-semibold hover:underline flex items-center relative z-20">
              Review &rarr;
            </button>
          </div>
        </div>
      </SortableItem>
    ),
    'metric-users': (
      <SortableItem id="metric-users" key="metric-users" className={WIDGET_CLASSES['metric-users']}>
        <div className="dark:bg-slate-800 bg-white border dark:border-slate-700 border-slate-200 rounded-2xl p-5 shadow-sm flex flex-col w-full h-full cursor-grab active:cursor-grabbing">
          <div className="flex justify-between items-start mb-2">
            <div className="w-10 h-10 dark:bg-purple-900/50 bg-purple-50 rounded-lg flex items-center justify-center">
              <Users className="dark:text-purple-400 text-purple-600 w-5 h-5" />
            </div>
            <div className="dark:bg-purple-900/50 bg-purple-100 dark:text-purple-400 text-purple-700 text-[10px] font-bold px-2 py-1 rounded-full">
              Live Staff
            </div>
          </div>
          <div className="mt-2">
            <p className="text-xs font-medium dark:text-slate-400 text-slate-500 mb-1">Users Online</p>
            <h2 className="text-2xl sm:text-3xl font-black dark:text-white text-slate-900 tracking-tight flex items-baseline">
              5 <span className="text-sm font-medium dark:text-slate-500 text-slate-400 ml-1">Active Now</span>
            </h2>
          </div>
          <div className="mt-auto pt-5 flex justify-between items-center">
            <div className="flex -space-x-2">
              <div className="w-6 h-6 rounded-full bg-blue-500 border border-white dark:border-slate-800 flex items-center justify-center text-[9px] text-white font-bold">DI</div>
              <div className="w-6 h-6 rounded-full bg-purple-500 border border-white dark:border-slate-800 flex items-center justify-center text-[9px] text-white font-bold">M</div>
              <div className="w-6 h-6 rounded-full bg-amber-500 border border-white dark:border-slate-800 flex items-center justify-center text-[9px] text-white font-bold">ES</div>
            </div>
            <Link to="/users" className="dark:text-purple-400 text-purple-600 text-xs font-semibold hover:underline relative z-20" onClick={(e) => e.stopPropagation()}>
              Roster
            </Link>
          </div>
        </div>
      </SortableItem>
    ),
    'metric-alerts': (
      <SortableItem id="metric-alerts" key="metric-alerts" className={WIDGET_CLASSES['metric-alerts']}>
        <div className="dark:bg-slate-800 bg-white border dark:border-slate-700 border-slate-200 rounded-2xl p-5 shadow-sm flex flex-col w-full h-full cursor-grab active:cursor-grabbing">
          <div className="flex justify-between items-start mb-2">
            <div className="w-10 h-10 dark:bg-red-900/50 bg-red-50 rounded-lg flex items-center justify-center">
              <ShieldAlert className="dark:text-red-400 text-red-500 w-5 h-5" />
            </div>
            <div className="dark:bg-red-900/50 bg-red-100 dark:text-red-400 text-red-700 text-[10px] font-bold px-2 py-1 rounded-full">
              Action Needed
            </div>
          </div>
          <div className="mt-2">
            <p className="text-xs font-medium dark:text-slate-400 text-slate-500 mb-1">System Alerts</p>
            <h2 className="text-2xl sm:text-3xl font-black dark:text-white text-slate-900 tracking-tight flex items-baseline">
              {3 * tfMult} <span className="text-sm font-medium dark:text-slate-500 text-slate-400 ml-1">Open Issues</span>
            </h2>
          </div>
          <div className="mt-auto pt-5 flex justify-between items-center">
            <div className="flex gap-2">
              <span className="dark:bg-red-900/50 bg-red-100 dark:text-red-400 text-red-700 text-[10px] px-1.5 py-0.5 rounded font-semibold">{1 * tfMult} Crit</span>
              <span className="dark:bg-amber-900/50 bg-amber-100 dark:text-amber-400 text-amber-700 text-[10px] px-1.5 py-0.5 rounded font-semibold">{2 * tfMult} Warn</span>
            </div>
            <button className="dark:text-slate-400 text-slate-500 text-xs hover:underline decoration-slate-400 underline-offset-2 relative z-20">
              Dismiss
            </button>
          </div>
        </div>
      </SortableItem>
    ),
    'chart-revenue': (
      <SortableItem id="chart-revenue" key="chart-revenue" className={WIDGET_CLASSES['chart-revenue']}>
        <div className="dark:bg-slate-800 bg-white border dark:border-slate-700 border-slate-200 rounded-3xl p-6 shadow-sm flex flex-col w-full h-full cursor-grab active:cursor-grabbing">
          <div className="flex justify-between items-center mb-1">
            <div className="flex items-center gap-3">
              <h2 className="text-lg sm:text-xl font-bold dark:text-white text-slate-900">Revenue Overview</h2>
              <span className="dark:bg-blue-900/50 bg-blue-50 dark:text-blue-400 text-blue-600 text-xs font-semibold px-2.5 py-0.5 rounded-full border dark:border-blue-800 border-blue-100">Live Feed</span>
            </div>
            <div className="flex dark:bg-slate-900 bg-slate-50 rounded-lg p-1 border dark:border-slate-700 border-slate-200 relative z-20" onPointerDown={(e) => e.stopPropagation()}>
              <button 
                onClick={() => setTimeFilter('Today')}
                className={`px-3 py-1 text-xs font-bold rounded shadow-sm border transition-colors ${timeFilter === 'Today' ? 'dark:bg-slate-800 bg-white dark:text-blue-400 text-blue-600 dark:border-slate-600 border-slate-200' : 'border-transparent dark:text-slate-400 text-slate-500 hover:text-slate-700'}`}
              >Today</button>
              <button 
                onClick={() => setTimeFilter('7 Days')}
                className={`px-3 py-1 text-xs font-bold rounded shadow-sm border transition-colors ${timeFilter === '7 Days' ? 'dark:bg-slate-800 bg-white dark:text-blue-400 text-blue-600 dark:border-slate-600 border-slate-200' : 'border-transparent dark:text-slate-400 text-slate-500 hover:text-slate-700'}`}
              >7 Days</button>
              <button 
                onClick={() => setTimeFilter('30 Days')}
                className={`px-3 py-1 text-xs font-bold rounded shadow-sm border transition-colors ${timeFilter === '30 Days' ? 'dark:bg-slate-800 bg-white dark:text-blue-400 text-blue-600 dark:border-slate-600 border-slate-200' : 'border-transparent dark:text-slate-400 text-slate-500 hover:text-slate-700'}`}
              >30 Days</button>
            </div>
          </div>
          <p className="text-xs dark:text-slate-400 text-slate-500 mb-8">Real-time gross passenger fares & collection analytics</p>
          
          <div className="relative h-64 w-full mb-6 relative z-10" onPointerDown={(e) => e.stopPropagation()}>
            <div className="absolute top-0 left-0 flex items-center dark:text-slate-500 text-slate-400 text-xs">
              <Info className="w-3.5 h-3.5 mr-1" />
              Hover across timeline curve for interval revenue breakdown
            </div>
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={mockRevenueData} margin={{ top: 30, right: 10, left: -20, bottom: 0 }}>
                <defs>
                  <linearGradient id="colorRevenue" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.3}/>
                    <stop offset="95%" stopColor="#3b82f6" stopOpacity={0}/>
                  </linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#334155" opacity={0.2} />
                <XAxis dataKey="time" axisLine={false} tickLine={false} tick={{ fontSize: 10, fill: '#64748b' }} dy={10} />
                <YAxis axisLine={false} tickLine={false} tick={{ fontSize: 10, fill: '#64748b' }} tickFormatter={(val) => `₱${val/1000}k`} />
                <Tooltip 
                  contentStyle={{ borderRadius: '12px', border: 'none', boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)', backgroundColor: 'var(--tw-colors-slate-800)', color: 'white' }}
                  formatter={(value) => [`₱${value.toLocaleString()}`, 'Revenue']}
                />
                <Area type="monotone" dataKey="value" stroke="#3b82f6" strokeWidth={3} fillOpacity={1} fill="url(#colorRevenue)" dot={{ stroke: '#3b82f6', strokeWidth: 2, fill: '#fff', r: 4 }} activeDot={{ r: 6, strokeWidth: 0, fill: '#2563eb' }} />
              </AreaChart>
            </ResponsiveContainer>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mt-auto border-t dark:border-slate-700 border-slate-100 pt-5">
            <div className="flex items-center gap-3 dark:bg-slate-900/50 bg-slate-50/50 rounded-xl p-3 border dark:border-slate-700 border-slate-100">
              <div className="w-10 h-10 dark:bg-blue-900/50 bg-blue-50 dark:text-blue-400 text-blue-500 rounded-lg flex items-center justify-center shrink-0">
                <TrendingUp className="w-5 h-5" />
              </div>
              <div>
                <p className="text-[10px] dark:text-slate-400 text-slate-500 font-medium">Average Per Trip</p>
                <p className="text-base font-bold dark:text-white text-slate-900 flex items-baseline gap-1">
                  ₱384 <span className="text-[10px] text-emerald-500">+5.4%</span>
                </p>
              </div>
            </div>
            
            <div className="flex items-center gap-3 dark:bg-slate-900/50 bg-slate-50/50 rounded-xl p-3 border dark:border-slate-700 border-slate-100">
              <div className="w-10 h-10 dark:bg-emerald-900/50 bg-emerald-50 dark:text-emerald-400 text-emerald-500 rounded-lg flex items-center justify-center shrink-0">
                <Activity className="w-5 h-5" />
              </div>
              <div>
                <p className="text-[10px] dark:text-slate-400 text-slate-500 font-medium">Total Trips Completed</p>
                <p className="text-base font-bold dark:text-white text-slate-900 flex items-baseline gap-1">
                  {324 * tfMult} <span className="text-[10px] dark:text-slate-500 text-slate-400 font-normal">dispatches</span>
                </p>
              </div>
            </div>

            <div className="flex items-center gap-3 dark:bg-slate-900/50 bg-slate-50/50 rounded-xl p-3 border dark:border-slate-700 border-slate-100">
              <div className="w-10 h-10 dark:bg-amber-900/50 bg-amber-50 dark:text-amber-400 text-amber-500 rounded-lg flex items-center justify-center shrink-0">
                <Fuel className="w-5 h-5" />
              </div>
              <div>
                <p className="text-[10px] dark:text-slate-400 text-slate-500 font-medium">Fuel Efficiency</p>
                <p className="text-base font-bold dark:text-white text-slate-900 flex items-baseline gap-1">
                  4.2 km/L <span className="text-[9px] font-bold dark:text-emerald-400 text-emerald-600 dark:bg-emerald-900/50 bg-emerald-100 px-1 py-0.5 rounded">Euro-4 OK</span>
                </p>
              </div>
            </div>
          </div>
        </div>
      </SortableItem>
    ),
    'chart-fleet': (
      <SortableItem id="chart-fleet" key="chart-fleet" className={WIDGET_CLASSES['chart-fleet']}>
        <div className="dark:bg-slate-800 bg-white border dark:border-slate-700 border-slate-200 rounded-3xl p-6 shadow-sm flex flex-col items-center w-full h-full cursor-grab active:cursor-grabbing">
          <div className="w-full flex justify-between items-center mb-6">
            <h2 className="text-lg font-bold dark:text-white text-slate-900 flex items-center gap-1">
              Fleet Health Score <Info className="w-3.5 h-3.5 dark:text-slate-500 text-slate-400" />
            </h2>
            <span className="dark:bg-emerald-900/50 bg-emerald-50 dark:text-emerald-400 text-emerald-600 text-xs font-semibold px-2.5 py-0.5 rounded-full border dark:border-emerald-800 border-emerald-100">Good Standby</span>
          </div>
          
          <div className="relative w-48 h-48 mb-4" onPointerDown={(e) => e.stopPropagation()}>
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={pieData}
                  cx="50%"
                  cy="50%"
                  innerRadius={70}
                  outerRadius={90}
                  paddingAngle={2}
                  dataKey="value"
                  stroke="none"
                  cornerRadius={4}
                >
                  {pieData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                  ))}
                </Pie>
              </PieChart>
            </ResponsiveContainer>
            <div className="absolute inset-0 flex flex-col items-center justify-center pointer-events-none">
              <span className="text-3xl font-black dark:text-white text-slate-900">85%</span>
              <span className="text-[9px] font-bold dark:text-slate-500 text-slate-500 tracking-wider">FLEET INDEX</span>
            </div>
          </div>

          <p className="text-[11px] dark:text-slate-400 text-slate-500 text-center mb-6 px-4">
            20 of 25 Modern PUVs road-ready for peak commute
          </p>

          <div className="w-full grid grid-cols-2 gap-3 mb-6">
            <div className="dark:bg-emerald-900/20 bg-emerald-50/50 border dark:border-emerald-900/50 border-emerald-100 rounded-lg p-2.5 flex justify-between items-center">
              <div className="flex items-center text-xs font-medium dark:text-slate-300 text-slate-700">
                <div className="w-2 h-2 rounded-full bg-emerald-500 mr-2"></div>
                Good
              </div>
              <span className="text-xs font-bold dark:text-emerald-400 text-emerald-700">{good} units</span>
            </div>
            
            <div className="dark:bg-amber-900/20 bg-amber-50/50 border dark:border-amber-900/50 border-amber-100 rounded-lg p-2.5 flex justify-between items-center">
              <div className="flex items-center text-xs font-medium dark:text-slate-300 text-slate-700">
                <div className="w-2 h-2 rounded-full bg-amber-500 mr-2"></div>
                Warning
              </div>
              <span className="text-xs font-bold dark:text-amber-400 text-amber-700">{warn} units</span>
            </div>

            <div className="dark:bg-red-900/20 bg-red-50/50 border dark:border-red-900/50 border-red-100 rounded-lg p-2.5 flex justify-between items-center">
              <div className="flex items-center text-xs font-medium dark:text-slate-300 text-slate-700">
                <div className="w-2 h-2 rounded-full bg-red-500 mr-2"></div>
                Critical
              </div>
              <span className="text-xs font-bold dark:text-red-400 text-red-700">{crit} units</span>
            </div>

            <div className="dark:bg-slate-700/20 bg-slate-50 border dark:border-slate-700/50 border-slate-200 rounded-lg p-2.5 flex justify-between items-center">
              <div className="flex items-center text-xs font-medium dark:text-slate-300 text-slate-700">
                <div className="w-2 h-2 rounded-full bg-slate-400 mr-2"></div>
                Idle
              </div>
              <span className="text-xs font-bold dark:text-slate-400 text-slate-600">{idle} units</span>
            </div>
          </div>

          <Link to="/maintenance" className="w-full mt-auto dark:bg-slate-900 bg-slate-50 hover:bg-slate-100 dark:hover:bg-slate-700 dark:text-slate-300 text-slate-700 text-xs font-bold py-3 rounded-xl flex items-center justify-center border dark:border-slate-700 border-slate-200 transition-colors relative z-20" onClick={(e) => e.stopPropagation()}>
            View Fleet Report <span className="ml-1">&gt;</span>
          </Link>
        </div>
      </SortableItem>
    ),
    'chart-dispatches': (
      <SortableItem id="chart-dispatches" key="chart-dispatches" className={WIDGET_CLASSES['chart-dispatches']}>
        <div className="dark:bg-slate-800 bg-white border dark:border-slate-700 border-slate-200 rounded-3xl p-6 shadow-sm flex flex-col w-full h-full cursor-grab active:cursor-grabbing">
          <div className="flex justify-between items-center mb-1">
            <h2 className="text-lg font-bold dark:text-white text-slate-900 flex items-center gap-2">
              <Activity className="w-5 h-5 dark:text-blue-400 text-blue-500" />
              Active Dispatches
            </h2>
            <span className="text-xs font-semibold dark:text-slate-400 text-slate-500 bg-slate-100 dark:bg-slate-900 px-2.5 py-1 rounded-full">{dateStr}</span>
          </div>
          
          <div className="flex flex-col gap-3 overflow-y-auto pr-1 relative z-20 mt-4" style={{ maxHeight: '350px' }} onPointerDown={(e) => e.stopPropagation()}>
            {MOCK_DISPATCHES.map((driver) => (
              <div key={driver.id} className="flex flex-col p-3 rounded-2xl border dark:border-slate-700 border-slate-100 dark:bg-slate-900/50 bg-slate-50 dark:hover:bg-slate-700 hover:bg-slate-100 hover:border-slate-200 transition-colors cursor-pointer">
                <div className="flex items-center">
                  <img src={driver.avatar} alt={driver.name} className="w-12 h-12 rounded-full border-2 dark:border-slate-800 border-white shadow-sm mr-4" />
                  <div className="flex-1 min-w-0">
                    <h4 className="text-sm font-bold dark:text-white text-slate-900 truncate">{driver.name}</h4>
                    <p className="text-[11px] font-medium dark:text-slate-400 text-slate-500 truncate flex items-center gap-1 mt-0.5">
                      <Truck className="w-3 h-3 dark:text-slate-500 text-slate-400" /> {driver.vehicle}
                    </p>
                  </div>
                </div>
                <div className="flex items-center justify-between mt-3 pt-3 border-t dark:border-slate-700 border-slate-200/60">
                  <span className="text-[10px] font-semibold dark:text-blue-400 text-blue-600 truncate dark:bg-blue-900/30 bg-blue-50 px-2 py-0.5 rounded-full inline-block">
                    {driver.route}
                  </span>
                  <span className="text-[10px] font-medium dark:text-slate-400 text-slate-500 flex items-center">
                    <TrendingUp className="w-3 h-3 mr-1 dark:text-slate-500 text-slate-400"/>
                    {driver.schedule}
                  </span>
                </div>
              </div>
            ))}
          </div>
        </div>
      </SortableItem>
    )
  };

  return (
    <DndContext sensors={sensors} collisionDetection={closestCenter} onDragEnd={handleDragEnd}>
      <div className="space-y-6">
        <SortableContext items={widgetOrder} strategy={rectSortingStrategy}>
          <div className="grid grid-cols-12 gap-5 grid-flow-row-dense">
            {widgetOrder.map(id => widgets[id])}
          </div>
        </SortableContext>
      </div>
    </DndContext>
  );
};

export default SuperAdminDashboard;
"""

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(new_content)

