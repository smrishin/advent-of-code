ranges = []
rangeString = ""

with open('input.txt', 'r') as file:
    for line in file:
        rangeString = line.split(",")


for r in rangeString:
    a,b = r.split("-")
    ranges.append((int(a), int(b)))

# print(ranges)

res = 0

def check_pattern(s) -> bool:
    # if len(s) % 2:
    #     return False
    patterns = {}

    for i in range(len(s)//2):
        patterns[s[:i+1]] = 0

    for p in patterns:
        l = len(p)
        intp = int(p)
        for j in range(0, len(s), l):
            # print(s[j:j+l])
            if intp == int(s[j:j+l]):
                patterns[p] += 1
        if (patterns[p] * l) == len(s):
            return True
        # print(l, ">>>>>>>>>>>>>>")
    # print (s, patterns)
    
    
    return False


for r in ranges:
    print(f"starting for {r}")
    id = r[0]
    end = r[1]

    while id <= end:

        if check_pattern(str(id)):
            res += id

        id += 1
    print(f"ending {r} with res as {res}")


print(res)