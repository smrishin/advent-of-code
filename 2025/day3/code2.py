# Took a little help from AI to figure out the code for this monotonic stack problem

banks = []

with open('input.txt', 'r') as file:
    for line in file:
        # print(line.strip())
        banks.append(line.strip())

max_joltage = []

def largest_joltage(s):
    # no of batteries to remove, total - 12, cuz we keep 12
    remove = len(s) - 12
    stack = []

    for i in s:
        while remove > 0 and stack and stack[-1] < i:
            stack.pop()
            remove -= 1
        stack.append(i)
    
    while remove > 0:
        stack.pop()
        remove -= 1
    
    return int(''.join(stack[:12]))


for bank in banks:
    joltage = largest_joltage(bank)
    max_joltage.append(joltage)



print(max_joltage)

output_joltage = sum(max_joltage)

print(output_joltage)