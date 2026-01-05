from typing import List

inputs: List[str] = []

with open('input.txt', 'r') as file:
    for line in file:
        # print(line.strip())
        inputs.append(line.strip())

nice_count = 0
for val in inputs:
    val = val.lower()

    vowels = {'a', 'e', 'i', 'o', 'u'}
    invalid_identifiers = {'ab', 'cd', 'pq', 'xy'}

    vowels_count = 0
    is_double_letter = False
    invalid = False

    if val[-1] in vowels:
        vowels_count += 1

    i = 0
    while i + 1 < len(val):
        double_letter = val[i] + val[i+1]

        if double_letter in invalid_identifiers:
            invalid = True
            break

        if val[i] in vowels:
            vowels_count += 1
        
        if val[i] == val[i+1]:
            is_double_letter = True
        i += 1

    if not invalid and vowels_count >= 3 and is_double_letter:
        nice_count += 1

print(f"There are {nice_count} nice strings")

