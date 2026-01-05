inputs = []

with open('input.txt', 'r') as file:
    for line in file:
        # print(line.strip())
        inputs.append(line.strip())

total = 0
for val in inputs:
    l, w, h = list(map(int, val.split("x")))

    a = 2 * (l + w)
    b = 2 * (w + h)
    c = 2 * (l + h)

    perimeter = min(a, b, c)
    vol = l * w * h
    total += perimeter + vol

print(total)

