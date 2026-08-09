input_file = 'input.txt'

def parse_input(input_file):
    passphrases = []
    with open(input_file, 'r') as file:
        for line in file:
            # print(line.strip())
            row = line.strip().split()
            passphrases.append(row)
    return passphrases

def check_unique_words(input_file):
    passphrases = parse_input(input_file)
    res = 0

    for l in passphrases:
        if len(l) == len(set(l)):
            res += 1

    return res

solution = check_unique_words(input_file)

print(f"Number of paraphrases without duplicates are {solution}")
print(f"Answer is {solution}")

