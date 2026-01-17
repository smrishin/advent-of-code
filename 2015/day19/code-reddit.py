# https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4cu5b/

from random import shuffle

input_file = 'input.txt'

def parse_input(input_file):
    replacements = []
    end_molecule = ""
    with open(input_file, 'r') as file:
        breakFound = False
        for line in file:
            # print(line.strip())
            if line.strip() == "":
                breakFound = True
                continue
            if breakFound:
                end_molecule = line.strip()
                continue
            parts = line.strip().split()
            replacement = (parts[0], parts[2])
            replacements.append(replacement)

    return replacements, end_molecule


reps, mol = parse_input(input_file)

target = mol
part2 = 0

while target != 'e':
    tmp = target
    for a, b in reps:
        if b not in target:
            continue

        target = target.replace(b, a, 1)
        part2 += 1

    if tmp == target:
        target = mol
        part2 = 0
        shuffle(reps)

print(part2)