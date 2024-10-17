from grid import Grid
from elements import Cquad4, Ctria3, Cbush
#
def reader_main(model):
    fem_file = open(model, "r")
    fem_file_list = fem_file.readlines()
    fem_file.close()
    nodes = {}
    elements = {}
    index = 0
    while index < len(fem_file_list):
        temp_line = fem_file_list[index]
        if "\t" in temp_line:
            temp_line = temp_line.expandtabs()
        if temp_line.strip()[:8] == "GRID    ":
            nodes[int(temp_line[8:16].strip())] = Grid(temp_line.strip())
        elif temp_line.strip()[:8] == "CQUAD4  ":
            temp_eid = int(temp_line.strip()[8:16].strip())
            elements[temp_eid] = Cquad4(temp_line.strip())
        elif temp_line.strip()[:8] == "CTRIA3  ":
            temp_eid = int(temp_line[8:16].strip())
            elements[temp_eid] = Ctria3(temp_line.strip())
        elif temp_line.strip()[:8] == "CBUSH   ":
            temp_eid = int(temp_line[8:16].strip())
            lines = [temp_line]
            index += 1
            temp_line = fem_file_list[index]
            if "\t" in temp_line:
                temp_line = temp_line.expandtabs()
            if (temp_line[:8].strip() == "" or temp_line[:8].strip() == "+") and temp_line[8:48] != "":
                lines.append(temp_line)
            else:
                index -= 1
            elements[temp_eid] = Cbush(lines)
        else:
            pass
#
        index += 1
    output_list = {}
    output_list["nodes"] = nodes
    output_list["elements"] = elements
    return output_list
