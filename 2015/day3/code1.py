inputs = []

with open('input.txt', 'r') as file:
    for line in file:
        # print(line.strip())
        inputs.append(line.strip())

for input in inputs:
    x = 0
    y = 0
    visited = {(x,y)}

    directions = {
        "^": (0,1),
        "v": (0,-1),
        ">": (1,0),
        "<": (-1,0)
    }

    for dir in input:
        x += directions.get(dir, (0,0))[0]
        y += directions.get(dir, (0,0))[1]
        visited.add((x,y))

    print(f"{len(visited)} houses recieved at least 1 present")


