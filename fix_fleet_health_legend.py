import re

with open('frontend/src/pages/SuperAdminDashboard.jsx', 'r') as f:
    content = f.read()

# Let's verify and just leave the Legend and remove anything extra. 
# It seems correct now, there's just the Legend (4 items) below the bar, which is compact and perfect.

# The user said: "On the fleet health score. I need to see a health bar for the units. Not total health bar. I still see the indicators text below bloating it."
# Maybe they don't even want the legend? Let's check image 2. 
# Image 2 shows exactly what was removed (the 4 large boxes). So removing those boxes addresses the "bloating" issue. 
