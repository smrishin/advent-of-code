
input_file = 'input.txt'

R = 5
C = 5
keypad =    [
    ['#','#','1','#','#'],
    ['#','2','3','4','#'],
    ['5','6','7','8','9'],
    ['#','A','B','C','#'],
    ['#','#','D','#','#']
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

def make_a_move(curr, row, col):
    nrow = row + moves[curr][0]
    ncol = col + moves[curr][1]

    if 0 <= nrow < R and 0 <= ncol < C and keypad[nrow][ncol] != '#':
        return nrow, ncol

    return row, col

def find_bathroom_code(input_file):
    instructions = parse_input(input_file)
    row = 2
    col = 0
    code = ""
    for ins in instructions:
        for i in ins:
            row, col = make_a_move(i, row, col)
        code += keypad[row][col]

    return code

solution = find_bathroom_code(input_file)

print(f"Bathroom code is {solution}")
print(f"Answer is {solution}")

