from float_converter import float_converter
#
class Pcomp():
    def __init__(self, lines):
        self.lines = lines
        self.type = "PCOMP"
        self.pid = None
        self.z0 = None
        self.plies = []
        self.read_1st_line()
        for temp in lines[1:]:
            self.read_other_lines(temp)
    def read_1st_line(self):
        self.pid = int(self.lines[0][8:16])
        self.z0 = float_converter(self.lines[0][16:24])
        return
    def read_other_lines(self, ply_line):
        temp_mat = int(ply_line[8:16])
        temp_thickness = float(ply_line[16:24])
        temp_angle = int(float(ply_line[24:32]))
        self.plies.append({"mat":temp_mat, "t":temp_thickness, "angle":temp_angle})
        if len(ply_line) > 40:
            temp_mat = int(ply_line[40:48])
            temp_thickness = float(ply_line[48:56])
            temp_angle = int(float(ply_line[56:64]))
            self.plies.append({"mat":temp_mat, "t":temp_thickness, "angle":temp_angle})
        return
class Pbush():
    def __init__(self, lines):
        self.lines = lines
        self.type = "PBUSH"
        self.pid = int(self.lines[0][8:16])
        self.k1 = None
        self.k2 = None
        self.k3 = None
        self.k4 = None
        self.k5 = None
        self.k6 = None
        self.b1 = None
        self.b2 = None
        self.b3 = None
        self.b4 = None
        self.b5 = None
        self.b6 = None
        self.ge1 = None
        self.ge2 = None
        self.ge3 = None
        self.ge4 = None
        self.ge5 = None
        self.ge6 = None
        self.sa = None
        self.st = None
        self.ea = None
        self.et = None
        self.m = None
        for reading_line in self.lines:
            if reading_line[16:24].strip() == "K":
                self.read_k(reading_line)
            elif reading_line[16:24].strip() == "B":
                self.read_b(reading_line)
            elif reading_line[16:24].strip() == "GE":
                self.read_ge(reading_line)
            elif reading_line[16:24].strip() == "RCV":
                self.read_rcv(reading_line)
            elif reading_line[16:24].strip() == "M":
                self.read_m(reading_line)
    def read_k(self, temp_line):
        if temp_line[24:32].strip() != "":
            self.k1 = float_converter(temp_line[24:32])
        if temp_line[32:40].strip() != "":
            self.k2 = float_converter(temp_line[32:40])
        if temp_line[40:48].strip() != "":
            self.k3 = float_converter(temp_line[40:48])
        if temp_line[48:56].strip() != "":
            self.k4 = float_converter(temp_line[48:56])
        if temp_line[56:64].strip() != "":
            self.k5 = float_converter(temp_line[56:64])
        if temp_line[64:72].strip() != "":
            self.k6 = float_converter(temp_line[64:72])
        return
    def read_b(self, temp_line):
        if temp_line[24:32].strip() != "":
            self.b1 = float_converter(temp_line[24:32])
        if temp_line[32:40].strip() != "":
            self.b2 = float_converter(temp_line[32:40])
        if temp_line[40:48].strip() != "":
            self.b3 = float_converter(temp_line[40:48])
        if temp_line[48:56].strip() != "":
            self.b4 = float_converter(temp_line[48:56])
        if temp_line[56:64].strip() != "":
            self.b5 = float_converter(temp_line[56:64])
        if temp_line[64:72].strip() != "":
            self.b6 = float_converter(temp_line[64:72])
        return
    def read_ge(self, temp_line):
        if temp_line[24:32].strip() != "":
            self.ge1 = float_converter(temp_line[24:32])
        if temp_line[32:40].strip() != "":
            self.ge2 = float_converter(temp_line[32:40])
        if temp_line[40:48].strip() != "":
            self.ge3 = float_converter(temp_line[40:48])
        if temp_line[48:56].strip() != "":
            self.ge4 = float_converter(temp_line[48:56])
        if temp_line[56:64].strip() != "":
            self.ge5 = float_converter(temp_line[56:64])
        if temp_line[64:72].strip() != "":
            self.ge6 = float_converter(temp_line[64:72])
        return
    def read_rcv(self, temp_line):
        if temp_line[24:32].strip() != "":
            self.sa = float_converter(temp_line[24:32])
        if temp_line[32:40].strip() != "":
            self.st = float_converter(temp_line[32:40])
        if temp_line[40:48].strip() != "":
            self.ea = float_converter(temp_line[40:48])
        if temp_line[48:56].strip() != "":
            self.et = float_converter(temp_line[48:56])
        return
    def read_m(self, temp_line):
        if temp_line[24:32].strip() != "":
            self.m = float_converter(temp_line[24:32])
        return
