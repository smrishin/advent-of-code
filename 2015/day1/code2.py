inputs = []

with open('input.txt', 'r') as file:
    for line in file:
        # print(line.strip())
        inputs.append(line.strip())


for val in inputs:
    res = 0
    for i, val in enumerate(val):
        if val == "(":
            res += 1
        elif val == ")":
            res -= 1
        if res == -1:
            print(f"Santa first enters the basement at {i + 1} position")
            break
    
    # print(f"Instruction takes Santa to {res} floor" )
    