from laminate import Laminate
from failure_criterias import yamada_sun
#
def CLA(laminate_input, load_input):
    laminate_input.calc_laminate_stress_strain(load_input, True)
    rf_list = []
    output_file = open("CLA_output.fnx", "w")
    output_file.write(f"Stacking: {laminate_input.stacking}\n\n")
    output_file.write(f"Material: {laminate_input.material}\n\n")
    output_file.write("PLY"+"<>"+"Bot_RF    "+"<>"+"Top_RF"+"\n")
    for index, temp_ply in enumerate(laminate_input.plies):
        temp_bottom_rf = yamada_sun(temp_ply.bottom_stress_loc[0], 
                                    temp_ply.bottom_stress_loc[2], 
                                    temp_ply.material)
        temp_top_rf = yamada_sun(temp_ply.bottom_stress_loc[0], 
                                 temp_ply.bottom_stress_loc[2], 
                                 temp_ply.material)
        rf_list.append({"bottom":temp_bottom_rf,
                        "top":temp_top_rf})
        output_file.write(str(index+1).ljust(3)+"<>"
                          + str(round(temp_bottom_rf,4)).ljust(10)+"<>"+
                          str(round(temp_top_rf,4)).ljust(10)+"\n")
    output_file.close()
    return rf_list
###
if __name__ == "__main__":
    #stacking = "90/45/0/135/135/0/45/90"
    stacking = "0/30/60"
    load = [100, 100, 100, 0, 0, 0]
    material = "AS_8552"
    the_laminate = Laminate(stacking, material)
    CLA(the_laminate, load)

