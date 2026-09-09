with open('frontend/src/components/notifications/NotificationDropdown.jsx', 'r') as f:
    content = f.read()

content = content.replace(
    "const NotificationDropdown = ({ notifications, onMarkAllAsRead, onMarkAsRead }) => {",
    "const NotificationDropdown = ({ notifications, onMarkAllAsRead, onMarkAsRead, onClose }) => {"
)

content = content.replace(
    "    if (n.type) {\n      // Pass the notification ID to highlight it on the target page\n      navigate(`/${n.type}`, { state: { highlightId: n._id } });\n    }\n  };",
    "    if (n.type) {\n      // Pass the notification ID to highlight it on the target page\n      navigate(`/${n.type}`, { state: { highlightId: n._id } });\n    }\n    if (onClose) {\n      onClose();\n    }\n  };"
)

with open('frontend/src/components/notifications/NotificationDropdown.jsx', 'w') as f:
    f.write(content)
