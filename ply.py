import numpy as np
from material import assign_material
class Ply:
    def __init__(self, angle_in, mat_in):
        self.angle = angle_in
        self.angle_rad = np.deg2rad(self.angle)
        self.cos = np.cos(self.angle_rad)
        self.sin = np.sin(self.angle_rad)
        if type(mat_in) == str:
            self.material = assign_material(mat_in)
        elif type(mat_in) == dict:
            self.material = assign_material("User Defined")
            self.material.t_ply = mat_in["t_ply"]
            self.material.e_1 = mat_in["e_1"]
            self.material.e_2 = mat_in["e_2"]
            self.material.nu_12 = mat_in["nu_12"]
            self.material.g_12 = mat_in["g_12"]
            self.material.calc_n21()
        self.thickness = self.material.t_ply
        self.q11 = None
        self.q12 = None
        self.q22 = None
        self.q66 = None
        self.generate_q_local()
        self.q_glob = None
        self.calc_q_glob()
        self.transform_matrix = np.array([[self.cos**2,self.sin**2,2*self.cos*self.sin],
                                          [self.sin**2,self.cos**2,-2*self.cos*self.sin],
                                          [-self.cos*self.sin,self.cos*self.sin,self.cos**2-self.sin**2]])
        self.top_stress_glob = None
        self.bottom_stress_glob = None
        self.top_strain_glob = None
        self.bottom_strain_glob = None
        self.top_stress_loc = None
        self.bottom_stress_loc = None
        self.top_strain_loc = None
        self.bottom_strain_loc = None
    def generate_q_local(self):
        self.q11 = self.material.e_1 / (1 - self.material.nu_12 * self.material.nu_21)
        self.q12 = self.material.e_2 * self.material.nu_12 / (1 - self.material.nu_12 * self.material.nu_21)
        self.q22 = self.material.e_2 / (1 - self.material.nu_12 * self.material.nu_21)
        self.q66 = self.material.g_12
        return
    def calc_q_glob(self):
        m = self.cos
        n = self.sin
        q_11 = self.q11*m**4+2*(self.q12+2*self.q66)*m**2*n**2+self.q22*n**4
        q_12 = (self.q11+self.q22-4*self.q66)*m**2*n**2+self.q12*(m**4+n**4)
        q_22 = self.q11*n**4+2*(self.q12+2*self.q66)*m**2*n**2+self.q22*m**4
        q_16 = (self.q11-self.q12-2*self.q66)*m**3*n+(self.q12-self.q22+2*self.q66)*m*n**3
        q_26 = (self.q11-self.q12-2*self.q66)*n**3*m+(self.q12-self.q22+2*self.q66)*n*m**3
        q_66 = (self.q11+self.q22-2*self.q12-2*self.q66)*m**2*n**2+self.q66*(m**4+n**4)
        self.q_glob = np.array([[q_11, q_12, q_16],
                         [q_12, q_22, q_26],
                         [q_16, q_16, q_66]])
        return