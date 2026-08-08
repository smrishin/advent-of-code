
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

def find_diff(sheet):
    res = 0
    for r in sheet:
        low, high = r[0], r[0]
        for i in r[1:]:
            if i < low:
                low = i
            elif i > high:
                high = i
        
        res += high - low

    return res

def checksum(input_file):
    sheet = parse_input(input_file)
    res = find_diff(sheet)

    return res

solution = checksum(input_file)

print(f"Checksum is {solution}")
print(f"Answer is {solution}")

