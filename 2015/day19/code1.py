import re

input_file = 'input.txt'

def parse_input(input_file):
    replacements = []
    start_molecule = ""
    with open(input_file, 'r') as file:
        breakFound = False
        for line in file:
            # print(line.strip())
            if line.strip() == "":
                breakFound = True
                continue
            if breakFound:
                start_molecule = line.strip()
                continue
            parts = line.strip().split()
            replacement = (parts[0], parts[2])
            replacements.append(replacement)

    return replacements, start_molecule

def replace_molecules(start_molecule, replacements):
    distinct_molecules = set()

    for r in replacements:
        for match in re.finditer(r[0], start_molecule):
            start, end = match.span()
            # print(f"Match found: {match.group()}, Position: {start}, {end}")
            new_molecule = start_molecule[:start] + r[1] + start_molecule[end:]
            # print(new_molecule)
            distinct_molecules.add(new_molecule)
    return distinct_molecules


def molecule_replacement(input_file):
    replacements, start_molecule = parse_input(input_file)
    
    # for l in replacements:
    #     print(l)
    # print(f"start {start_molecule}")

    distinct_molecules = replace_molecules(start_molecule, replacements)
    return len(distinct_molecules)

solution = molecule_replacement(input_file) 

print(f"{solution} distinct molecules can be created")
print(f"Answer is {solution}")
