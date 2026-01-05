inputs = []

with open('input.txt', 'r') as file:
    for line in file:
        # print(line.strip())
        inputs.append(line.strip())

for input in inputs:
    x = 0
    y = 0
    rx = 0
    ry = 0
    visited = {(x,y)}

    directions = {
        "^": (0,1),
        "v": (0,-1),
        ">": (1,0),
        "<": (-1,0)
    }

    i = 0
    while i < len(input):
        x += directions.get(input[i], (0,0))[0]
        y += directions.get(input[i], (0,0))[1]
        visited.add((x,y))
        i += 1

        if i >= len(input):
            break

        rx += directions.get(input[i], (0,0))[0]
        ry += directions.get(input[i], (0,0))[1]
        visited.add((rx,ry))
        i += 1


    print(f"{len(visited)} houses recieved at least 1 present")


