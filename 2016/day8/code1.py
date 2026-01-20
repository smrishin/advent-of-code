import sys
input_file = 'input.txt'

R = 6 #3
C = 50 #7

def print_display(disp):
    # print("NEXT DISPLAY")
    for r in range(R):
        print(''.join(disp[r]))
    
def parse_input(input_file):
    instructions = []
    with open(input_file, 'r') as file:
        for line in file:
            # print(line.strip())
            instructions.append(line.strip())
    return instructions

def add_rect(disp, r, c):
    # print("add_rect", r, c)
    for cr in range(r):
        for cc in range(c):
            disp[cr][cc] = '#'
    return disp

def rotate_col(disp, c, off):
    # print("rotate_col", c, off)
    curr_col = []
    for r in range(R):
        curr_col.append(disp[r][c])
    new_col = curr_col[-off:] + curr_col[:-off]
    for r in range(R):
        disp[r][c] = new_col[r]
    return disp

def rotate_row(disp, r, off):
    # print("rotate_row", r, off)
    curr_row = disp[r]
    new_row = curr_row[-off:] + curr_row[:-off]
    disp[r] = new_row
    return disp

def process_ins(ins, disp):
    if 'rect' in ins:
        _, dimen = ins.split()
        c, r = map(int, dimen.split('x'))
        add_rect(disp, r, c)
    if "column" in ins:
        _, right = ins.split('=')
        c, off = map(int, right.split(" by "))
        rotate_col(disp, c, off)
    if "row" in ins:
        _, right = ins.split('=')
        r, off = map(int, right.split(" by "))
        rotate_row(disp, r, off)
    return disp

def count_lit_pixels(disp):
    count = 0
    for r in range(R):
        for c in range(C):
            if disp[r][c] == '#':
                count += 1
    return count

def small_screen_display(input_file):
    instructions = parse_input(input_file)
    display = [["."] * C for _ in range(R)]
    print("Initial Display")
    print_display(display)

    for ins in instructions:
        # print(ins)
        process_ins(ins, display)

    print("Final Display")
    print_display(display)

    return count_lit_pixels(display)

solution = small_screen_display(input_file)

print(f"{solution} pixels are lit")
print(f"Answer is {solution}")
