import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

fleet_bottom_regex = r'          <div className="w-full grid grid-cols-2 gap-3 mb-6 pointer-events-auto">.*?<div className="flex items-center text-xs font-medium dark:text-slate-300 text-slate-700">.*?Critical.*?</div>\s*<span className="text-xs font-bold dark:text-red-400 text-red-700">\{crit\} units</span>\s*</div>\s*</div>'

# Let's replace the whole grid starting at: <div className="w-full grid grid-cols-2 gap-3 mb-6 pointer-events-auto">
# up to the end of the widget

# Actually, I can use a simpler replacement if I just grab the marker.
marker_start = '          <div className="w-full grid grid-cols-2 gap-3 mb-6 pointer-events-auto">'

parts = content.split(marker_start)
if len(parts) == 2:
    end_marker = '        </div>\n          ),\n    \'chart-dispatches\':'
    # wait, the chart-dispatches starts after chart-fleet in widgetContents
    
    # Just grab everything up to chart-dispatches
    parts2 = parts[1].split('          ),\n    \'chart-dispatches\':')
    if len(parts2) == 2:
        new_content = parts[0] + '        </div>\n          ),\n    \'chart-dispatches\':' + parts2[1]
        with open('frontend/src/pages/SuperAdminDashboard.jsx', 'w') as f:
            f.write(new_content)
