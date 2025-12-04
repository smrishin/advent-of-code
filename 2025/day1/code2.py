res = 0

curr = 50

with open('input.txt', 'r') as file:
    for line in file:
        # print(line.strip())
        no_of_rotations = int(line[1:])
        for i in range(no_of_rotations):
            if line[0] == "L":
                curr -= 1
            else:
                curr += 1
            if curr % 100 == 0:
                res += 1
        print(line, curr%100, res, "\n")
        

print(res)    
