nums = []
ops = []

with open('input.txt', 'r') as file:
    content = []
    for line in file:
        content.append(line[:-1])
    
    nums = content[:-1]
    ops = content[-1]

    
ops = ops.split()
# print(ops)
# for num in nums:
#     print(num)

op_id = 0
grand_total = 0

buffer = []
for vals in zip(*nums):
    new_val = ''.join(vals).strip()
    # print(new_val)
    if new_val == "":
        exp = ops[op_id].join(buffer)
        grand_total += eval(exp)
        buffer = []
        op_id += 1
    else:
        buffer.append(new_val)
exp = ops[op_id].join(buffer)
grand_total += eval(exp)

print(f"Grand total is {grand_total}")