inputs = []

with open('input.txt', 'r') as file:
    for line in file:
        # print(line.strip())
        inputs.append(line.strip())

total = 0
for input in inputs:
    l, w, h = list(map(int, input.split("x")))

    a = l * w
    b = w * h
    c = l * h

    area = 2 * (a + b + c)
    total += area + min(a,b,c)

print(total)

