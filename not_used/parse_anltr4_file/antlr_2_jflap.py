import re
from random import randint

with open("/home/user/LaTeX.g4") as f:
    latex_g4 = f.read()

labels = re.findall("(.*?):.*?;\n", latex_g4, re.DOTALL)
labels = [x.strip() for x in labels if x if "//" not in str(x) and " " not in str(x)]
terminal_group_labels = [x for x in labels if not re.findall("[a-z]", x)]
non_terminals = [x for x in labels if x not in terminal_group_labels]

mapping = {}
map_name_to_id = {}
counter = 0
parsed_g4 = re.findall("(.*?):(.*?);\n", latex_g4, re.DOTALL)

for line in parsed_g4[2:]:
    value = line[1].strip().replace("'", "")
    key = line[0].strip()
    values = [x.strip() for x in re.split("\s+\|\s+|\(|\)|\n", value) if x]
    mapping[key] = values


def print_state(idx, name, x_coord, y_coord):
    f = f"""<state id="{idx}" name="{name}">
                            <x>{x_coord}</x>
                            <y>{y_coord}</y>
                    </state>
        """
    return f


def print_transitions(src, dst, edge_string):
    t = f"""<transition>
            <from>{src}</from>
            <to>{dst}</to>
            <read>{edge_string}</read>
            </transition>
            """
    return t


header = """<?xml version="1.0" encoding="UTF-8" standalone="no"?><!--Created with JFLAP 7.1.--><structure>
    <type>fa</type>
    <automaton>
"""


def write_jflap_files(file_name):
    f = open(file_name, "w")
    return f


f = write_jflap_files("test.jff")
f.write(header)
f.write("\n")
current_x_coord_lside = 50
current_y_coord_lside = -300
current_y_coord_rside = 50
seen = set()
for idx, k in enumerate(set(mapping.keys())):
    if k in terminal_group_labels and k not in seen:
        map_name_to_id[k] = idx
        s = print_state(
            idx,
            k,
            current_x_coord_lside + 600 + randint(-200, 200),
            current_y_coord_rside,
        )
        current_y_coord_rside -= 50
        seen.add(k)
        f.write(s)
        f.write("\n")
        continue
    elif k in non_terminals and k not in terminal_group_labels and k not in seen:
        map_name_to_id[k] = idx
        s = print_state(idx, k, current_x_coord_lside, current_y_coord_lside)
        current_y_coord_lside -= 50
        seen.add(k)
        f.write(s)
        f.write("\n")
        continue

for key in mapping.keys():
    if key in non_terminals:
        match = [x for x in mapping[key] if x in terminal_group_labels]
        if match:
            for dst in [x for x in match]:
                s = print_transitions(map_name_to_id[key], map_name_to_id[dst], dst)
                f.write(s)
                f.write("\n")
f.write("</automaton>")
f.write("\n")
f.write("</structure>")
f.close()
