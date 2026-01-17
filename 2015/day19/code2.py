# Solved this with a little help from reddit
# https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/

from heapq import heappush, heappop

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

def molecule_replacement(input_file):
    '''
    start from the end molecule, replace b with a from given a => b
    pick the molecule with shortest length for next interation (greedy)
    until 'e' is reached
    '''

    replacements, end_molecule = parse_input(input_file)
    start_molecule = "e"
    
    # for l in replacements:
    #     print(l)
    # print(f"start {end_molecule}")


    heap = [] #(len(molecule), steps, molecule)
    heappush(heap, (len(end_molecule), 0, end_molecule))

    while heap:
        prev_len, prev_steps, prev_molecule = heappop(heap)

        # if the molecule cannot be created then this will break the inifite loop
        if prev_steps >= 210:
            break

        if prev_molecule == start_molecule:
            return prev_steps

        for a, b in replacements:
            if b not in prev_molecule:
                continue

            new_molecule = prev_molecule.replace(b, a, 1)
            heappush(heap, (len(new_molecule), prev_steps + 1, new_molecule))

    return -1

solution = molecule_replacement(input_file) 

print(f"{solution} steps to create the end molecules from 'e'")
print(f"Answer is {solution}")