
input_file = 'input.txt'

'''
directions index : direction
0 : NORTH
1 : EAST
2 : SOUTH
3 : WEST
'''

directions = [(0,1),(1,0),(0,-1),(-1,0)]



def parse_input(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            # print(line.strip())
            instructions = line.strip().split(", ")
    return instructions

def follow_next_instruction(ins, curr_location, curr_direction):
    if ins[0] == "R":
        curr_direction = (curr_direction + 1) % 4
    else:
        curr_direction = (curr_direction - 1) % 4

    blocks_to_walk = int(ins[1:])
    x = curr_location[0] + (directions[curr_direction][0] * blocks_to_walk)
    y = curr_location[1] + (directions[curr_direction][1] * blocks_to_walk)
    return (x,y), curr_direction

def find_shortest_path(input_file):
    instructions = parse_input(input_file)
    initial_location = (0,0)
    curr_direction = 0
    curr_location = (0,0)
    for ins in instructions:
        curr_location, curr_direction = follow_next_instruction(ins, curr_location, curr_direction)

    return abs(curr_location[0] - initial_location[0]) + abs(curr_location[1] - initial_location[1])

solution = find_shortest_path(input_file)

print(f"Destination is {solution} blocks away")
print(f"Answer is {solution}")

