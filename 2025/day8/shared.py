from heapq import heappush, heappop

def load_and_sort_points(file_name):
    points = []

    with open(file_name, 'r') as file:
        for line in file:
            # print(line.strip())
            input = line.strip().split(',')
            points.append(list(map(int, input)))

    # for point in points:
    #     print(point)

    heap = []

    # Find the distances and store them in heap
    for i in range(len(points)):
        for j in range(i+1, len(points)):        
            dist = 0
            for a, b in zip(points[i], points[j]):
                dist += (a - b) ** 2

            heappush(heap, (dist, i, j)) # tuple(points[i]), tuple(points[j])))        
    return points, heap

# UNION FIND SOLUTION BETTER MAYBE

def make_union(n):
    parent = {i:i for i in range(n)}
    rank = {i:0 for i in range(n)}
    def find_parent(n):
        while parent[n] != n:
            parent[n] = parent[parent[n]]
            n = parent[n]
        return n

    def union(n1, n2):
        p1, p2 = find_parent(n1), find_parent(n2)

        if p1 == p2:
            return False
        
        if rank[p1] > rank[p2]:
            parent[p2] = p1
        elif rank[p2] > rank[p1]:
            parent[p1] = p2
        else:
            parent[p1] = p2
            rank[p2] += 1
        return True
    return parent, rank, find_parent, union
