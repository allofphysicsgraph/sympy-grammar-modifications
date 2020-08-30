grammar_file_path='LaTeX_v1.g4'
with open(grammar_file_path) as f:
    latex_g4 = f.read()

labels = re.findall("(.*?):.*?;\n", latex_g4, re.DOTALL)
labels = [x.strip() for x in labels if x if "//" not in str(x) and " " not in str(x)]
terminal_group_labels = [x for x in labels if not re.findall("[a-z]", x)]
non_terminals = [x for x in labels if x not in terminal_group_labels]

mapping = {}
map_name_to_id = {}
counter = 0
parsed_g4 = re.findall("(.*?):(.*?);\n", latex_g4, re.DOTALL)

remove =set()

for line in parsed_g4[2:]:
    value = line[1].strip().replace("'", "")
    key = line[0].strip()
    values = [x.strip() for x in re.split("\s+\|\s+|\(|\)|\n", value) if x]
    mapping[key] = values

for k,v in mapping.items():
    if k!='UNKNOWN':
        for word in v:
            if word in mapping['UNKNOWN']:
                remove.add(word)
