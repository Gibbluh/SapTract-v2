import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

dispatches_old = r"""    'chart-dispatches': \(.*?<div className="flex justify-between items-center mb-1">.*?<h2 className="text-lg font-bold dark:text-white text-slate-900 flex items-center gap-2">.*?<Activity className="w-5 h-5 dark:text-blue-400 text-blue-500" />.*?Today's Driver.*?</h2>.*?<span className="text-xs font-semibold dark:text-slate-400 text-slate-500 bg-slate-100 dark:bg-slate-900 px-2\.5 py-1 rounded-full">\{dateStr\}</span>.*?</div>.*?<div className="flex flex-col gap-3 overflow-y-auto pr-1 relative z-20 mt-4".*?</div>.*?</div>"""

dispatches_new = """    'chart-dispatches': (
        <div className="dark:bg-slate-800 bg-white border dark:border-slate-700 border-slate-200 rounded-3xl p-6 shadow-sm flex flex-col w-full h-full cursor-grab active:cursor-grabbing pointer-events-auto">
          <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-4 gap-3">
            <h2 className="text-lg font-bold dark:text-white text-slate-900 flex items-center gap-2">
              <Activity className="w-5 h-5 dark:text-blue-400 text-blue-500" />
              Today's Dispatches
            </h2>
            
            {/* Driver / Unit Tabs */}
            <div className="flex bg-slate-100 dark:bg-slate-900/50 p-1 rounded-lg border border-slate-200 dark:border-slate-700 pointer-events-auto" onPointerDown={(e) => e.stopPropagation()}>
              <button
                onClick={() => setDriverTab('Drivers')}
                className={`flex items-center px-4 py-1.5 text-xs font-bold rounded-md transition-colors ${driverTab === 'Drivers' ? 'bg-white dark:bg-slate-700 text-blue-600 dark:text-blue-400 shadow-sm' : 'text-slate-500 hover:text-slate-700 dark:hover:text-slate-300'}`}
              >
                <Users className="w-3 h-3 mr-1.5" /> Drivers (14)
              </button>
              <button
                onClick={() => setDriverTab('Units')}
                className={`flex items-center px-4 py-1.5 text-xs font-bold rounded-md transition-colors ${driverTab === 'Units' ? 'bg-white dark:bg-slate-700 text-blue-600 dark:text-blue-400 shadow-sm' : 'text-slate-500 hover:text-slate-700 dark:hover:text-slate-300'}`}
              >
                <Truck className="w-3 h-3 mr-1.5" /> Units (25)
              </button>
            </div>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mt-2 overflow-y-auto pr-1 pb-2 relative z-20" onPointerDown={(e) => e.stopPropagation()}>
            {driverTab === 'Drivers' ? MOCK_DISPATCHES.map((driver) => (
              <div key={driver.id} className="flex flex-col items-center p-4 rounded-2xl border dark:border-slate-700 border-slate-200 dark:bg-slate-900/50 bg-slate-50/50 dark:hover:bg-slate-800 hover:bg-white hover:border-blue-300 dark:hover:border-blue-500/50 transition-all cursor-pointer shadow-sm group">
                <div className="relative mb-3">
                  <img src={driver.avatar} alt={driver.name} className="w-16 h-16 rounded-full object-cover border-4 dark:border-slate-800 border-white shadow-md group-hover:scale-105 transition-transform" />
                  <span className="absolute bottom-0 right-0 w-4 h-4 rounded-full bg-emerald-500 border-2 border-white dark:border-slate-800"></span>
                </div>
                <h4 className="text-sm font-bold dark:text-white text-slate-900 text-center">{driver.name}</h4>
                <p className="text-[10px] font-semibold dark:text-blue-400 text-blue-600 mb-3 text-center">{driver.route}</p>
                
                <div className="w-full flex justify-between items-center pt-3 border-t dark:border-slate-700 border-slate-200/60 mt-auto">
                   <div className="flex flex-col">
                     <span className="text-[9px] font-bold dark:text-slate-500 text-slate-400 uppercase tracking-wider">Unit</span>
                     <span className="text-[11px] font-bold dark:text-slate-300 text-slate-700 flex items-center"><Truck className="w-3 h-3 mr-1 dark:text-slate-500 text-slate-400"/> {driver.vehicle}</span>
                   </div>
                   <button className="text-[10px] font-bold dark:bg-blue-900/30 bg-blue-50 dark:text-blue-400 text-blue-600 px-3 py-1.5 rounded-full hover:bg-blue-100 dark:hover:bg-blue-900/50 transition-colors">
                     View
                   </button>
                </div>
              </div>
            )) : MOCK_DISPATCHES.map((unit) => (
              <div key={unit.id} className="flex flex-col items-center p-4 rounded-2xl border dark:border-slate-700 border-slate-200 dark:bg-slate-900/50 bg-slate-50/50 dark:hover:bg-slate-800 hover:bg-white hover:border-emerald-300 dark:hover:border-emerald-500/50 transition-all cursor-pointer shadow-sm group">
                <div className="w-16 h-16 rounded-full dark:bg-emerald-900/30 bg-emerald-100 flex items-center justify-center mb-3 group-hover:scale-105 transition-transform border-4 dark:border-slate-800 border-white shadow-md relative">
                   <Truck className="w-7 h-7 dark:text-emerald-400 text-emerald-600" />
                   <span className="absolute bottom-0 right-0 w-4 h-4 rounded-full bg-emerald-500 border-2 border-white dark:border-slate-800"></span>
                </div>
                <h4 className="text-sm font-bold dark:text-white text-slate-900 text-center">{unit.vehicle}</h4>
                <p className="text-[10px] font-semibold dark:text-emerald-400 text-emerald-600 mb-3 text-center">{unit.route}</p>
                
                <div className="w-full flex justify-between items-center pt-3 border-t dark:border-slate-700 border-slate-200/60 mt-auto">
                   <div className="flex flex-col">
                     <span className="text-[9px] font-bold dark:text-slate-500 text-slate-400 uppercase tracking-wider">Driver</span>
                     <span className="text-[11px] font-bold dark:text-slate-300 text-slate-700 flex items-center"><Users className="w-3 h-3 mr-1 dark:text-slate-500 text-slate-400"/> {unit.name.split(' ')[0]}</span>
                   </div>
                   <button className="text-[10px] font-bold dark:bg-emerald-900/30 bg-emerald-50 dark:text-emerald-400 text-emerald-600 px-3 py-1.5 rounded-full hover:bg-emerald-100 dark:hover:bg-emerald-900/50 transition-colors">
                     View
                   </button>
                </div>
              </div>
            ))}
          </div>
        </div>"""

content = re.sub(dispatches_old, dispatches_new, content, flags=re.DOTALL)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
