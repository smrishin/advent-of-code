inputs = []

with open('input.txt', 'r') as file:
    for line in file:
        # print(line.strip())
        inputs.append(line.strip())


for val in inputs:
    res = 0
    for i in val:
        if i == "(":
            res += 1
        elif i == ")":
            res -= 1
    
    print(f"Instruction takes Santa to {res} floor" )
    