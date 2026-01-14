# used code from 2015/day9/code-reddit.py -Rishi

import sys
from itertools import permutations

people = set()
costs = dict()
for line in open('input.txt'):
    parts = line.split()
    source, dest = parts[0], parts[-1][:-1] #[:-1] to remove the . at the end of the line
    cost = int(parts[3]) if parts[2] == "gain" else (-1 * int(parts[3]))

    people.add(source)
    people.add(dest)
    
    costs_source = costs.setdefault(source, dict())
    costs_source.setdefault(dest, 0)
    costs[source][dest] += cost

    costs_dest = costs.setdefault(dest, dict())
    costs_dest.setdefault(source, 0)
    costs[dest][source] += cost


costs.setdefault("me", dict())
people.add("me")

for k in costs.keys():
    if k == "me":
        continue
    costs["me"].setdefault(k, 0)
    costs[k].setdefault("me", 0)

for k, v in costs.items():
    print(k, v)

longest = 0
best_seating = []
for items in permutations(people):
    first = items[0]
    last = items[-1]

    circular_cost = costs[first][last]
    costs_after_seating = list(map(lambda x, y: costs[x][y], items[:-1], items[1:]))
    costs_after_seating.append(circular_cost)


    total_cost = sum(costs_after_seating)
    if total_cost > longest:
        longest = total_cost
        best_seating = costs_after_seating[:]
# print(best_seating)
print("longest: %d" % (longest))