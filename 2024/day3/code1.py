import re
inputArr = []
pattern = re.compile("mul\(\d{1,3},\d{1,3}\)")
with open('input.txt', 'r') as file:
    content = file.read()
    # print(content)
    inputArr = re.findall(pattern, content)

# print(inputArr)

res = 0

for s in inputArr:
    a, b = s[4:-1].split(",")
    res += int(a) * int(b)

print(f"sum of all multiplications is {res}")
