import numpy as np
import pandas as pd
from ply import Ply
#
class Laminate():
    def __init__(self, stacking_str, mat_in):
        """
        plies = list
        """
        self.stacking = stacking_str
        self.material = mat_in
        stacking_list = self.stacking.split("/")
        self.plies = []
        for angle in stacking_list:
            self.plies.append(Ply(float(angle), mat_in))
        self.ply_number = len(self.plies)
        self.thickness = self.ply_number * self.plies[0].material.t_ply
        self.matrix_a = None
        self.matrix_b = None
        self.matrix_d = None
        self.calc_matrix()
        self.matrix_abd = np.vstack((np.hstack((self.matrix_a,self.matrix_b)),np.hstack((self.matrix_b,self.matrix_d))))
        self.matrix_abd_inv = np.linalg.inv(self.matrix_abd)
        self.e_x = 1 / self.matrix_abd_inv[0][0] / self.thickness
        self.e_y = 1 / self.matrix_abd_inv[1][1] / self.thickness
        self.g_xy = 1 / self.matrix_abd_inv[2][2] / self.thickness
        self.nu_xy = -self.matrix_abd_inv[0][1] / self.matrix_abd_inv[0][0]
        self.nu_yx = -self.matrix_abd_inv[0][1] / self.matrix_abd_inv[1][1]
    def calc_matrix(self):
        a = np.zeros((3, 3))
        b = np.zeros((3, 3))
        d = np.zeros((3, 3))
        z_lower = -self.thickness / 2
        for temp in self.plies:
            z_upper = z_lower + temp.thickness
            a += temp.q_glob * (z_upper - z_lower)
            b += temp.q_glob * (z_upper **2 - z_lower ** 2) / 2
            d += temp.q_glob * (z_upper **3 - z_lower ** 3) / 3
            z_lower = z_upper
        self.matrix_a = a
        self.matrix_b = b
        self.matrix_d = d
        return
    def calc_laminate_stress_strain(self, load, output_request):
        #calc layer strains global
        disp = np.dot(self.matrix_abd_inv, load)
        z = - self.thickness / 2
        strain = disp[:3]
        curvature = disp[3:]
        self.plies[0].bottom_strain_glob = list(strain + z * curvature)
        for i in range(self.ply_number - 1):
            z += self.plies[i].thickness
            self.plies[i].top_strain_glob = list(strain + z * curvature)
            self.plies[i + 1].bottom_strain_glob = list(strain + z * curvature)
        z += self.plies[-1].thickness
        self.plies[-1].top_strain_glob = list(strain + z * curvature)
        #calc layer stresses global
        for temp_ply in self.plies:
            temp_strain = temp_ply.bottom_strain_glob[:2] + [temp_ply.bottom_strain_glob[2] / 2]
            temp_stress1 = list(np.dot(temp_ply.q_glob, np.array(temp_strain)))
            temp_ply.bottom_stress_glob = temp_stress1[:2] + [temp_stress1[2] * 2]
            temp_strain = temp_ply.top_strain_glob[:2] + [temp_ply.top_strain_glob[2] / 2]
            temp_stress1 =  list(np.dot(temp_ply.q_glob, np.array(temp_strain)))
            temp_ply.top_stress_glob = temp_stress1[:2] + [temp_stress1[2] * 2]
        #calc local
        for index, temp_ply in enumerate(self.plies):
            t = self.plies[index].transform_matrix
            s = self.plies[index].bottom_strain_glob[:2]+[self.plies[index].bottom_strain_glob[-1]/2]
            t_s = np.dot(t, [[s[0]],[s[1]],[s[2]]])
            temp_strain_bottom = [t_s[0][0], t_s[1][0], t_s[2][0]]
            t = self.plies[index].transform_matrix
            s = self.plies[index].top_strain_glob[:2]+[self.plies[index].top_strain_glob[-1]/2]
            t_s = np.dot(t, [[s[0]],[s[1]],[s[2]]])
            temp_strain_top = [t_s[0][0], t_s[1][0], t_s[2][0]]
            temp_ply.bottom_strain_loc = temp_strain_bottom[:2]+[temp_strain_bottom[-1]*2]
            temp_ply.top_strain_loc = temp_strain_top[:2]+[temp_strain_top[-1]*2]
            t = self.plies[index].transform_matrix
            s = self.plies[index].bottom_stress_glob
            t_s = np.dot(t, [[s[0]],[s[1]],[s[2]]])
            temp_ply.bottom_stress_loc = [t_s[0][0], t_s[1][0], t_s[2][0]]
            t = self.plies[index].transform_matrix
            s = self.plies[index].top_stress_glob
            t_s = np.dot(t, [[s[0]],[s[1]],[s[2]]])
            temp_ply.top_stress_loc = [t_s[0][0], t_s[1][0], t_s[2][0]]
        if output_request:
            column_list = ["PLY", "Surface", "Epsilon_x", "Epsilon_y", "Gamma_xy",
                           "Sigma_x", "Sigma_y", "Tau_xy", "Epsilon_1", "Epsilon_2",
                           "Gamma_12", "Sigma_1", "Sigma_2", "Tau_12"]
            results = pd.DataFrame(columns = column_list)
            for index, temp_ply in enumerate(self.plies):
                temp = [index+1, "Bottom",
                        temp_ply.bottom_strain_glob[0],
                        temp_ply.bottom_strain_glob[1],
                        temp_ply.bottom_strain_glob[2],
                        temp_ply.bottom_stress_glob[0],
                        temp_ply.bottom_stress_glob[1],
                        temp_ply.bottom_stress_glob[2],
                        temp_ply.bottom_strain_loc[0],
                        temp_ply.bottom_strain_loc[1],
                        temp_ply.bottom_strain_loc[2],
                        temp_ply.bottom_stress_loc[0],
                        temp_ply.bottom_stress_loc[1],
                        temp_ply.bottom_stress_loc[2]]
                results.loc[len(results.index)] = temp
                temp = [index+1, "Top",
                        temp_ply.top_strain_glob[0],
                        temp_ply.top_strain_glob[1],
                        temp_ply.top_strain_glob[2],
                        temp_ply.top_stress_glob[0],
                        temp_ply.top_stress_glob[1],
                        temp_ply.top_stress_glob[2],
                        temp_ply.top_strain_loc[0],
                        temp_ply.top_strain_loc[1],
                        temp_ply.top_strain_loc[2],
                        temp_ply.top_stress_loc[0],
                        temp_ply.top_stress_loc[1],
                        temp_ply.top_stress_loc[2]]
                results.loc[len(results.index)] = temp
            writer = pd.ExcelWriter('stress_strain_output.xlsx')
            results.to_excel(writer, sheet_name="Results", index=False)
            writer.save()
        return
######
'''
#stacking_str = "90/45/0/135/135/0/45/90"
stacking_str = "0/90/0"
material = "DUMMY"
laminate = Laminate(stacking_str, material)
print(laminate.e_x)
print(laminate.e_y)
print(laminate.g_xy)
print(laminate.nu_xy)
'''
