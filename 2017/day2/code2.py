
input_file = 'input.txt'

def parse_input(input_file):
    sheet = []
    with open(input_file, 'r') as file:
        for line in file:
            # print(line.strip())
            row_str = line.strip().split()
            row = [int(x) for x in row_str]
            sheet.append(row)
    return sheet

def find_divisible_pairs(numbers):
    row_sum = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            a, b = numbers[i], numbers[j]

            if (b != 0 and a % b == 0):
                row_sum += a//b
            elif (a != 0 and b % a == 0):
                row_sum += b//a

    return row_sum

def find_checksum(sheet):
    res = 0
    for r in sheet:        
        res += find_divisible_pairs(r)

    return res

def checksum(input_file):
    sheet = parse_input(input_file)
    res = find_checksum(sheet)

    return res

solution = checksum(input_file)

print(f"Checksum is {solution}")
print(f"Answer is {solution}")

