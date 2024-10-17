from float_converter import float_converter
#
class Grid():
    def __init__(self, line):
        self.id = int(line[8:16].strip())
        try:
            self.cp = int(line[16:24].strip())
        except:
            self.cp = 0
        self.x = float_converter(line[24:32].strip())
        self.y = float_converter(line[32:40].strip())
        self.z = float_converter(line[40:48].strip())
        try:
            self.cd = int(line[48:56].strip())
        except:
            self.cd = 0
        try:
            self.ps = int(line[56:64].strip())
        except:
            self.ps = None
        try:
            self.seid = int(line[64:72].strip())
        except:
            self.seid = None






