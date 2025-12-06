ranges = []
rangeString = ""

with open('input.txt', 'r') as file:
    for line in file:
        rangeString = line.split(",")


for r in rangeString:
    a,b = r.split("-")
    ranges.append((int(a), int(b)))

print(ranges)

res = 0

for r in ranges:
    start = r[0]
    end = r[1]

    while start <= end:
        startStr = str(start)
        length = len(startStr)
        if length % 2 == 0:
            first = startStr[:length//2]
            last = startStr[length//2:]
            if first == last:
                res += start
        start +=1
print(res)