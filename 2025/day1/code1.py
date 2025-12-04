res = 0

curr = 50

with open('input.txt', 'r') as file:
    for line in file:
        # print(line.strip())
        if line[0] == "L":
            curr -= int(line[1:])
        else:
            curr += int(line[1:])
        if curr % 100 == 0:
            res += 1

print(res)    
