from heapq import heappush, heappop
from collections import defaultdict
from shared import load_and_sort_points, make_union

points, heap = load_and_sort_points("input.txt")
parent, rank, find_parent, union = make_union(len(points))

connections_to_make = 1000 # 10 # for testing its 10

count = 0

while heap and count < connections_to_make:
    dist, a, b = heappop(heap)   
    # print(a, b, dist) 
    # print(f"{a} + {b}")
    union_res = union(a, b)
    # if union_res:
    #     components -= 1
    count += 1

    # print(components)

freq_map = defaultdict(list)
for k in parent.keys():
    # There might be some components that arent compressed all the way 
    # to the parent, so we compress there before final count of circuits
    root = find_parent(k) 
    freq_map[root].append(k)

# c = 0
# for k, v in freq_map.items():
#     c += 1
#     print(f"GROUP {c}: {k} : {len(v)}")
#     print(v)
#     print("<<<<<<<<<<<<<<<<<<<<")

sizes = sorted([len(v) for k,v in freq_map.items()], reverse=True)
# print(sizes)

res = 1
for i in range(3):
    res *= sizes[i]
print(f"Multiply together the sizes of the three largest circuits will be {res}")