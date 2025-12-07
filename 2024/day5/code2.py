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

bad_updates = []
# filter bad and good updates
for u in updates:
    curr = u.split(",")
    # print(curr)
    if curr[0] not in order_map:
        bad_updates.append(curr)
        continue

    good_update = True
    for i in range(1, len(curr)):
        for j in range(i):
            if curr[i] not in order_map[curr[j]]:
                good_update = False
                break

        if not good_update:
            break

    if not good_update:
        bad_updates.append(curr)


# fix bad updates
for b in bad_updates:
    # print(b)
    n = len(b)
    fixed = [""] * n
    for val in b:
        other_vals_after = 0
        for other in b:
            if val != other and other in order_map[val]:
                other_vals_after += 1
        fixed[n-other_vals_after-1] = val
    print(fixed)
    res += int(fixed[n//2])

        
print(f"{res} is the sum of the middle page number after correcting the bad-ordered updates")