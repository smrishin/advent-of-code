banks = []

with open('input.txt', 'r') as file:
    for line in file:
        # print(line.strip())
        banks.append(line.strip())

max_joltage = []

for bank in banks:
    max1 = ['0',-1] #max num and its location
    max2 = ['0',-1] #max num and its location
    for i in range(len(bank)):
        if bank[i] > max1[0]:
            max1[0] = bank[i]
            max1[1] = i

    if max1[1] == len(bank) - 1:
        max2 = max1
        max1 = ['0',-1]
        for i in range(len(bank)-1):
            if bank[i] > max1[0]:
                max1[0] = bank[i]
                max1[1] = i
    else:
        for i in range(max1[1]+1, len(bank)):
            if bank[i] > max2[0]:
                max2[0] = bank[i]
                max2[1] = i
    joltage = int(max1[0] + max2[0])
    max_joltage.append(joltage)



print(max_joltage)

output_joltage = sum(max_joltage)

print(output_joltage)