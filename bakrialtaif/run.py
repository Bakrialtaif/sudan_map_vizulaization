import os

from SudanMapSVG import SudanMapSVG

# Example JSON data
data = [

    {"state": "SD-DC", "color": "blue"},
    {"state": "SD-DE", "color": "blue"},
    {"state": "SD-DN", "color": "red"},
    {"state": "SD-DS", "color": "blue"},
    {"state": "SD-DW", "color": "yellow"},
    {"state": "SD-GD", "color": "blue"},
    {"state": "SD-GK", "color": "black"},
    {"state": "SD-GZ", "color": "blue"},
    {"state": "SD-KA", "color": "brown"},
    {"state": "SD-KH", "color": "blue"},
    {"state": "SD-KN", "color": "blue"},
    {"state": "SD-KS", "color": "white"},
    {"state": "SD-NB", "color": "grey"},
    {"state": "SD-NO", "color": "blue"},
    {"state": "SD-NR", "color": "green"},
    {"state": "SD-NW", "color": "blue"},
    {"state": "SD-RS", "color": "blue"},
    {"state": "SD-SI", "color": "gray"},

    # Add more data as needed
]

# Load SVG file
svg_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sudan_map.svg')

map_svg = SudanMapSVG(svg_file)
map_svg.update_states(data)
map_svg.compile_svg('updated_sudan_map.svg')