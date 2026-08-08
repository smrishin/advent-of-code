from collections import defaultdict
orders = []
updates = []
res = 0

with open('input.txt', 'r') as file:
    content = file.read().split("\n")
    indexof = content.index("")
    orders = content[:indexof]
    updates = content[indexof + 1:]

# for o in orders:
#     print(o)
# for u in updates:
#     print(u)

order_map = defaultdict(set)

for o in orders:
    a, b = o.split("|")
    order_map[a].add(b)

# for k,v in order_map.items():
#     print(f"{k} : {v}")


for u in updates:
    curr = u.split(",")
    # print(curr)
    if curr[0] not in order_map:
        continue

    good_update = True
    for i in range(1, len(curr)):
        for j in range(i):
            if curr[i] not in order_map[curr[j]]:
                good_update = False
                break

        if not good_update:
            break

    if good_update:
        # print("yes")
        # add to res
        l = 0
        r = len(curr)
        m = l + (r-l)//2
        res += int(curr[m])

print(f"{res} is the sum of the middle page number from those correctly-ordered updates")