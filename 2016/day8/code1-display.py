'''
The main functional logic is write by me
The display.py, display-renderer.py is pulled from ChatGPT
'''

import time
from display import run_display, Display, DisplayConfig

input_file = 'input.txt'

R = 6 #3
C = 50 #7

def print_display(disp):
    # print("NEXT DISPLAY")
    for r in range(R):
        print(''.join(str(disp[r])))

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
            disp[cr][cc] = 1 #'#'
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
            if disp[r][c] == 1:
                count += 1
    return count

def small_screen_display(display: Display) -> None:
    instructions = parse_input(input_file)
    grid = [[0] * C for _ in range(R)]

    display.update(grid)

    for ins in instructions:
        # print(ins)
        process_ins(ins, grid)
        display.update(grid)
        time.sleep(0.02)

    solution = count_lit_pixels(grid)

    print(f"{solution} pixels are lit")
    print(f"Answer is {solution}")

    # close window when done
    time.sleep(5) # close window after 5 s
    display.close()

if __name__ == "__main__":
    run_display(
        start_logic=small_screen_display,
        config=DisplayConfig(rows=R, cols=C, cell=20, title="My Grid")
    )