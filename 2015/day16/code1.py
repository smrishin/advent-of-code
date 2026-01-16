
ticker_tape = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

sues_list = []

def parse_input(input_file):
    with open(input_file, 'r') as file:
        for i, line in enumerate(file):
            # print(line.strip())
            parts = line.split()
            sue = {
                "id": int(parts[1][:-1]),
            }
            for i in range(2, len(parts), 2):
                sue[parts[i][:-1]] = int(parts[i + 1]) if i == len(parts) - 2 else int(parts[i + 1][:-1])

            sues_list.append(sue)



def find_aunt_sue(input_file):
    parse_input(input_file)
    for i in sues_list:
        matching_number = 0
        matched = [False, False, False]
        mismatch = False
        for t, val in ticker_tape.items():
            if False not in matched:
                break
            
            if matching_number > 2:
                mismatch = True
                break

            if t in i.keys():
                if val != i[t]:
                    mismatch = True
                    break
                matched[matching_number] = True
                matching_number += 1
        if mismatch == True:
            continue
        
        if False not in matched:
            return i['id']


    return 0


solution = find_aunt_sue('input.txt')

print(f"Aunt Sue {solution} gifted me the MFCSAM")

