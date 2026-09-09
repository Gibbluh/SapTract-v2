import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

fleet_old = r"""          <div className="relative w-48 h-48 mb-4".*?          <div className="w-full grid grid-cols-2 gap-3 mb-6">"""

fleet_new = """          <div className="w-full flex-1 flex flex-col justify-center mb-6 pointer-events-auto" onPointerDown={(e) => e.stopPropagation()}>
            <div className="flex justify-between items-end mb-2">
               <div className="flex flex-col">
                 <span className="text-4xl font-black dark:text-white text-slate-900 tracking-tight">85%</span>
                 <span className="text-[10px] font-bold dark:text-slate-500 text-slate-400 tracking-wider">OVERALL INDEX</span>
               </div>
               <div className="text-right">
                 <p className="text-[11px] font-semibold dark:text-slate-300 text-slate-700">20 / 25 Units</p>
                 <p className="text-[10px] dark:text-slate-500 text-slate-500">Road-ready for peak commute</p>
               </div>
            </div>
            
            {/* Health Bar */}
            <div className="w-full h-4 rounded-full overflow-hidden flex bg-slate-100 dark:bg-slate-700 mt-4 mb-3 border dark:border-slate-600 border-slate-200">
              <div className="bg-emerald-500 h-full transition-all duration-500" style={{ width: `${(good/25)*100}%` }} title={`Good: ${good}`}></div>
              <div className="bg-amber-400 h-full transition-all duration-500 border-l dark:border-slate-800 border-white" style={{ width: `${(warn/25)*100}%` }} title={`Warning: ${warn}`}></div>
              <div className="bg-red-500 h-full transition-all duration-500 border-l dark:border-slate-800 border-white" style={{ width: `${(crit/25)*100}%` }} title={`Critical: ${crit}`}></div>
              <div className="bg-slate-400 dark:bg-slate-500 h-full transition-all duration-500 border-l dark:border-slate-800 border-white" style={{ width: `${(idle/25)*100}%` }} title={`Idle: ${idle}`}></div>
            </div>
            
            {/* Legend */}
            <div className="flex justify-between items-center text-[10px] font-medium px-1">
               <span className="flex items-center dark:text-slate-300 text-slate-600"><span className="w-2.5 h-2.5 rounded bg-emerald-500 mr-1.5 shadow-sm"></span> {good} Good</span>
               <span className="flex items-center dark:text-slate-300 text-slate-600"><span className="w-2.5 h-2.5 rounded bg-amber-400 mr-1.5 shadow-sm"></span> {warn} Warning</span>
               <span className="flex items-center dark:text-slate-300 text-slate-600"><span className="w-2.5 h-2.5 rounded bg-red-500 mr-1.5 shadow-sm"></span> {crit} Critical</span>
               <span className="flex items-center dark:text-slate-400 text-slate-500"><span className="w-2.5 h-2.5 rounded bg-slate-400 dark:bg-slate-500 mr-1.5 shadow-sm"></span> {idle} Idle</span>
            </div>
          </div>

          <div className="w-full grid grid-cols-2 gap-3 mb-6 pointer-events-auto">"""

content = re.sub(fleet_old, fleet_new, content, flags=re.DOTALL)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)
