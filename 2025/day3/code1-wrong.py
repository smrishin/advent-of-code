# Understood the question wrong first, solved it correctly in another file.
# This code might still be useful, hence saving it.


from heapq import heappush, heappop


banks = []

with open('testinput.txt', 'r') as file:
    for line in file:
        # print(line.strip())
        banks.append(line.strip())

max_joltage = []

for bank in banks:
    max_heap = []
    for i in range(len(bank)):
        heappush(max_heap, (-1*int(bank[i]), i))
    a, aPos = heappop(max_heap)
    b, bPos = heappop(max_heap)
    joltage = 0
    if aPos < bPos:
        joltage = -a*10 + -b
    else:
        joltage = -b*10 + -a

    max_joltage.append(joltage)



print(max_joltage)

output_joltage = sum(max_joltage)

print(output_joltage)