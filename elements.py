from float_converter import float_converter
#
class Cquad4():
    def __init__(self, line):
        self.type = "CQUAD4"
        self.eid = int(line[8:16].strip())
        self.pid = int(line[16:24].strip())
        self.g1 = int(line[24:32].strip())
        self.g2 = int(line[32:40].strip())
        self.g3 = int(line[40:48].strip())
        self.g4 = int(line[48:56].strip())
        if line[56:64].strip() != "":
            self.theta_mcid = float_converter(line[56:64].strip())
        else:
            self.theta_mcid = None
        if line[64:72].strip() != "":
            self.zoffs = float_converter(line[64:72].strip())
        else:
            self.zoffs = None
class Ctria3():
    def __init__(self, line):
        self.type = "CTRIA3"
        self.eid = int(line[8:16].strip())
        self.pid = int(line[16:24].strip())
        self.g1 = int(line[24:32].strip())
        self.g2 = int(line[32:40].strip())
        self.g3 = int(line[40:48].strip())
        if line[48:56].strip() != "":
            self.theta_mcid = float_converter(line[56:64].strip())
        else:
            self.theta_mcid = None
        if line[56:64].strip() != "":
            self.zoffs = float_converter(line[64:72].strip())
        else:
            self.zoffs = None
class Cbush():
    def __init__(self, lines):
        self.type = "CBUSH"
        self.eid = None
        self.pid = None
        self.ga = None
        self.gb = None
        self.go_x1 = None
        self.x2 = None
        self.x3 = None
        self.cid = None
        self.s = None
        self.ocid = None
        self.s1 = None
        self.s2 = None
        self.s3 = None
        if len(lines) == 1:
            self.read_line1(lines[0])
        else:
            self.read_line1(lines[0])
            self.read_line2(lines[1])
    def read_line1(self,temp_line):
        self.eid = int(temp_line[8:16].strip())
        self.pid = int(temp_line[16:24].strip())
        self.ga = int(temp_line[24:32].strip())
        self.gb = int(temp_line[32:40].strip())
        if temp_line[40:48].strip() != "":
            self.go_x1 = int(temp_line[40:48].strip())
        if temp_line[48:56].strip() != "":
            self.x2 = int(temp_line[48:56].strip())
        if temp_line[56:64].strip() != "":
            self.x3 = int(temp_line[56:64].strip())
        if temp_line[64:72].strip() != "":
            self.cid = int(temp_line[64:72].strip())
        return
    def read_line2(self,temp_line):
        if temp_line[8:16].strip() != "":
            self.s = float_converter(temp_line[8:16].strip())
        if temp_line[16:24].strip() != "":
            self.ocid = int(temp_line[16:24].strip())
        if temp_line[24:32].strip() != "":
            self.s1 = float_converter(temp_line[24:32].strip())
        if temp_line[32:40].strip() != "":
            self.s2 = float_converter(temp_line[32:40].strip())
        if temp_line[40:48].strip() != "":
            self.s3 = float_converter(temp_line[40:48].strip())
        return
