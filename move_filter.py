with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# Remove filter from Revenue Overview
filter_html = """            <div className="flex dark:bg-slate-900 bg-slate-50 rounded-lg p-1 border dark:border-slate-700 border-slate-200 relative z-20" onPointerDown={(e) => e.stopPropagation()}>
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
            </div>"""

content = content.replace(filter_html, "")

# Add it to the top of the dashboard
top_html = """  return (
    <DndContext sensors={sensors} collisionDetection={closestCenter} onDragEnd={handleDragEnd}>
      <div className="space-y-6">
        <div className="flex justify-between items-center bg-white dark:bg-slate-800 p-4 rounded-2xl border border-slate-200 dark:border-slate-700 shadow-sm">
          <h2 className="text-lg font-bold text-slate-900 dark:text-white">Dashboard Overview</h2>
          <div className="flex dark:bg-slate-900 bg-slate-50 rounded-lg p-1 border dark:border-slate-700 border-slate-200">
            <button 
              onClick={() => setTimeFilter('Today')}
              className={`px-4 py-1.5 text-xs font-bold rounded shadow-sm border transition-colors ${timeFilter === 'Today' ? 'dark:bg-slate-800 bg-white dark:text-blue-400 text-blue-600 dark:border-slate-600 border-slate-200' : 'border-transparent dark:text-slate-400 text-slate-500 hover:text-slate-700'}`}
            >Today</button>
            <button 
              onClick={() => setTimeFilter('7 Days')}
              className={`px-4 py-1.5 text-xs font-bold rounded shadow-sm border transition-colors ${timeFilter === '7 Days' ? 'dark:bg-slate-800 bg-white dark:text-blue-400 text-blue-600 dark:border-slate-600 border-slate-200' : 'border-transparent dark:text-slate-400 text-slate-500 hover:text-slate-700'}`}
            >7 Days</button>
            <button 
              onClick={() => setTimeFilter('30 Days')}
              className={`px-4 py-1.5 text-xs font-bold rounded shadow-sm border transition-colors ${timeFilter === '30 Days' ? 'dark:bg-slate-800 bg-white dark:text-blue-400 text-blue-600 dark:border-slate-600 border-slate-200' : 'border-transparent dark:text-slate-400 text-slate-500 hover:text-slate-700'}`}
            >30 Days</button>
          </div>
        </div>
        
        <SortableContext items={widgetOrder} strategy={rectSortingStrategy}>"""

content = content.replace("  return (\n    <DndContext sensors={sensors} collisionDetection={closestCenter} onDragEnd={handleDragEnd}>\n      <div className=\"space-y-6\">\n        <SortableContext items={widgetOrder} strategy={rectSortingStrategy}>", top_html)

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
    f.write(content)

