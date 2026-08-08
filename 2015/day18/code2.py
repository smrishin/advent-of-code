
input_file = 'input.txt'
steps_for_animation = 100 #5 #for testinput 5 steps
directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]

def parse_input(input_file):
    lights = []
    with open(input_file, 'r') as file:
        for line in file:
            # print(line.strip())
            row = list(line.strip())
            for i in range(len(row)):
                if row[i] == ".":
                    row[i] = 0
                else:
                    row[i] = 1
            lights.append(row)

    return lights

def change_lights(curr_lights):
    R = len(curr_lights)
    C = len(curr_lights[0])
    next_lights = [[0] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            # Part 2: light in the four corners cannot be turned off
            if r in [0, R-1] and c in [0, C-1]:
                next_lights[r][c] = 1
                continue

            total = 0

            for ro, co in directions:
                nr, nc = r + ro, c + co
                if (
                    0 <= nr < R and
                    0 <= nc < C
                    ):
                    total += curr_lights[nr][nc]

            if curr_lights[r][c] == 1:
                if total == 2 or total == 3:
                    next_lights[r][c] = 1
                else:
                    next_lights[r][c] = 0
            else:
                if total == 3:
                    next_lights[r][c] = 1
                else:
                    next_lights[r][c] = 0
    return next_lights

def turn_on_corner_lights(lights):
    R = len(lights)
    C = len(lights[0])

    for r in [0, R-1]:
        for c in [0, C-1]:
            lights[r][c] = 1
    return lights

def animate_lights(input_file, steps):
    lights = parse_input(input_file)

    # PART 2
    lights = turn_on_corner_lights(lights)

    for l in lights:
        print(l)
    
    for _ in range(steps):
        lights = change_lights(lights)

    # for l in lights:
    #     print(l)
    grand_total = 0
    for row in lights:
        grand_total += sum(row)
    return grand_total

solution = animate_lights(input_file, steps_for_animation) 

print(f"{solution} lights are on after {steps_for_animation} steps with all four corner lights never turned off")
print(f"Answer is {solution}")
