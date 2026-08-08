from heapq import heapify, heappop

listA = []
listB = []

with open('input.txt', 'r') as file:
    for line in file:
        # print(line.strip())
        a,b = line.strip().split("   ")
        listA.append(int(a))
        listB.append(int(b))

# print(listA)
# print(listB)

heapify(listA)
heapify(listB)

totalDist = 0


while listA and listB:
    a = heappop(listA)
    b = heappop(listB)
    # print(a,b)
    totalDist += abs(a - b)


print(f"total distrance is {totalDist}")