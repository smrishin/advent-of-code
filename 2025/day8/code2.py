from heapq import heappop
from shared import load_and_sort_points, make_union

points, heap = load_and_sort_points("input.txt")
parent, rank, find_parent, union = make_union(len(points))

components = len(points)
a, b = -1, -1
while heap and components > 1:
    dist, a, b = heappop(heap)   
    # print(a, b, dist) 
    # print(f"{a} + {b}")
    union_res = union(a, b)
    if union_res:
        components -= 1
    # print(components)
print(f"Multiply together the X coordinates of the last two junction boxes {points[a][0]*points[b][0]}")