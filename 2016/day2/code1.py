
input_file = 'input.txt'

keypad =    [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

moves = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0),
}


def parse_input(input_file):
    instructions = []
    with open(input_file, 'r') as file:
        for line in file:
            # print(line.strip())
            instructions.append(line.strip())
    return instructions

def make_moves(curr, size, row, col):
    # make moves
    nrow = row + size * moves[curr][0]
    ncol = col + size * moves[curr][1]

    # limits
    nrow = max(0, min(2, nrow))
    ncol = max(0, min(2, ncol))
    return nrow, ncol

def find_bathroom_code(input_file):
    instructions = parse_input(input_file)
    row = 1
    col = 1
    code = ""
    for ins in instructions:
        ins += "#"
        curr = ins[0]
        l = 0
        for r in range(len(ins)):
            if ins[r] != curr:
                # get the size of the curr ending window
                size = r - l
                row, col = make_moves(curr, size, row, col)
                # start next window
                curr = ins[r]
                l = r
            r += 1
        code += str(keypad[row][col])

    return code

solution = find_bathroom_code(input_file)

print(f"Bathroom code is {solution}")
print(f"Answer is {solution}")

