nums = []
ops = []

with open('input.txt', 'r') as file:
    content = []
    for line in file:
        # print(line.strip().split())
        content.append(line.strip().split())
    nums = content[:-1]
    ops = content[-1]
    


# print(nums)
# print(ops)

R = len(nums)
C = len(nums[0])

transpose = list(zip(*nums))
# print(transpose)

grand_total = 0
for vals, op in zip(transpose, ops):
    exp = op.join(vals)
    # print(exp)
        
    grand_total += eval(exp)

print(f"Grand total is {grand_total}")