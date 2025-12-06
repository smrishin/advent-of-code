from collections import Counter

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

countA = Counter(listA)
countB = Counter(listB)

score = 0 

for id in countA:
    curr = id * countA[id] * countB[id]
    score += curr


print(f"similarity score is {score}")