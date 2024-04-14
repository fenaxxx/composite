material_list = ["AS_123", "DUMMY", "User Defined"]
class As_8552:
    def __init__(self):
        self.name = "AS_123"
        self.t_ply = 123
        self.e_1 = 123
        self.e_2 = 123
        self.nu_12 = 0.123
        self.nu_21 =self.e_2 * self.nu_12 / self.e_1
        self.g_12 = 123
        self.f_1_t = 123
        self.f_1_c = 123
        self.f_2_t = 123
        self.f_2_c = 123
        self.f_3_t = 123
        self.f_3_c = 123
        self.f_12 = 123
        self.f_13 = 123
class Dummy:
    def __init__(self):
        self.name = "DUMMY1"
        self.t_ply = 123
        self.e_1 = 123
        self.e_2 = 123
        self.nu_12 = 0.123
        self.nu_21 =self.e_2 * self.nu_12 / self.e_1
        self.g_12 = 123
        self.f_1_t = 123
        self.f_1_c = 123
        self.f_2_t = 123
        self.f_2_c = 123
        self.f_3_t = 123
        self.f_3_c = 123
        self.f_12 = 123
        self.f_13 = 123
class User_Defined:
    def __init__(self):
        self.name = "User_Defined"
        self.t_ply = None
        self.e_1 =  None
        self.e_2 =  None
        self.nu_12 = None
        self.nu_21 = None
        self.g_12 =  None
        self.f_1_t =  None
        self.f_1_c =  None
        self.f_2_t =  None
        self.f_2_c =  None
        self.f_3_t =  None
        self.f_3_c =  None
        self.f_12 =  None
        self.f_13 =  None
    def calc_n21(self):
        self.nu_21 =self.e_2 * self.nu_12 / self.e_1
def assign_material(mat_name):
    if mat_name == "DUMMY1":
        return Dummy1()
    elif mat_name == "DUMMY2":
        return Dummy2()
    elif mat_name == "AS_8552":
        return As_8552()
    elif mat_name == "User Defined":
        return User_Defined()
    else:
        raise KeyError
