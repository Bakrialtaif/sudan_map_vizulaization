import xml.etree.ElementTree as ET

class SudanMapSVG:
    
    def __init__(self, svg_file):
        self.svg_file = svg_file
        self.tree = ET.parse(svg_file)
        self.root = self.tree.getroot()

    def update_states(self, data):
        for item in data:
            state_id = item['state']
            state_elem = self.root.find(".//*[@id='{}']".format(state_id))
            if state_elem is not None:
                state_elem.set('fill', item['color'])

    def compile_svg(self, output_file):
        self.tree.write(output_file)
