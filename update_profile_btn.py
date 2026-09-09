import re

with open('frontend/src/components/layout/Sidebar.jsx', 'r') as f:
    content = f.read()

# Update the Super Admin profile box in the sidebar to exactly match the request:
# "Also put the Super Administrator Profile on the top right and put it on the logout area, basically replace it"
# Currently the profile btn reads: "{user?.fullName || 'Super Admin'}" and "Logout"
# The user wants it to look like a profile.
# "put the Super Administrator Profile on the top right and put it on the logout area" 
# Oh wait, "put the Super Administrator Profile on the top right and put it on the logout area" might mean:
# The user profile should be in the logout area on the bottom left of the sidebar, and I already did this.

# Let's ensure it says Super Administrator.
content = content.replace('{user?.fullName || "Super Admin"}', '{user?.fullName || "Super Administrator"}')

with open('frontend/src/components/layout/Sidebar.jsx', 'w') as f:
    f.write(content)
