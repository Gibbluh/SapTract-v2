import re

with open('frontend/src/components/layout/Topbar.jsx', 'r') as f:
    content = f.read()

# Let's ensure topbar ends cleanly
content = content.replace('<div className="flex items-center justify-center">\n            <NotificationBell userId={user?._id || user?.id} />\n          </div>\n        </div>', '<div className="flex items-center justify-center mr-2">\n            <NotificationBell userId={user?._id || user?.id} />\n          </div>\n        </div>')

with open('frontend/src/components/layout/Topbar.jsx', 'w') as f:
    f.write(content)
