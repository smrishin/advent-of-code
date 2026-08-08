import re
inputArr = [] # {}

pattern = re.compile("mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)")

res = 0


with open('input.txt', 'r') as file:
    content = file.read()
    # print(content)

    enable_mul = True

    for m in re.findall(pattern, content):
        if m == "don't()":
            enable_mul = False
            continue
        elif m == "do()":
            enable_mul = True
            continue
        
        if enable_mul: 
            a, b = (map(int,m[4:-1].split(",")))
            res += a*b

print(f"sum of all multiplications is {res}")
