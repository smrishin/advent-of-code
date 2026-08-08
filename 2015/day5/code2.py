from typing import List, Dict

inputs: List[str] = []

with open('input.txt', 'r') as file:
    for line in file:
        # print(line.strip())
        inputs.append(line.strip())

nice_count = 0
for val in inputs:
    val = val.lower()

    pairs_last_loc: Dict[str, int] = {}

    pair_dup_exists = False
    dup_with_one_in_between = False

    i = 0
    while i + 1 < len(val):
        pair = val[i] + val[i+1]
        if pair in pairs_last_loc:
            if i - pairs_last_loc[pair] >= 2:
                pair_dup_exists = True
                break
        else:
            pairs_last_loc[pair] = i
        i += 1

    i = 0
    while i + 2 < len(val):
        if val[i] == val[i + 2]:
            dup_with_one_in_between = True
            break
        i += 1

    
    if pair_dup_exists and dup_with_one_in_between:
        nice_count += 1


print(f"There are {nice_count} nice strings")

