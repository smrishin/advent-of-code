points = []
with open("input.txt", 'r') as file:
    for line in file:
        # print(line.strip())
        input = line.strip().split(',')
        points.append(list(map(int, input)))
print(points)

maxarea = 0
n = len(points)
for i in range(n):
    for j in range(i + 1, n):
        A = points[i]
        B = points[j]
        area = ((A[0] - B[0]) + 1) * ((A[1] - B[1]) + 1)
        maxarea = max(maxarea, area)        
print(maxarea)