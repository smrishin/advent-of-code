reslights = []
buttons = []
lights = []

with open("testinput.txt", "r") as file:
    for line in file:
        # print(line.strip().split(" "))
        reslights.append(list(line.strip().split("]")[0][1:]))
        buttons.append(line.strip().split(" ")[1:-1])

for l in reslights:
    n = len(l)
    initial_lights = ["."] * n
    lights.append(initial_lights)

print(reslights)
print(lights)
print(buttons)

# Bitwise operators. i barely have any knowledge on this