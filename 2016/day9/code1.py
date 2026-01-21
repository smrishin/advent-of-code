input_file = 'input.txt'

def parse_input(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            # print(line.strip())
            return line.strip()

def decompress_data(compressed):
    decompressed = ""
    i = 0
    charlen = 0
    prev_loc = -1
    multiplier = 0
    in_marker = False
    decompressing = False
    while i < len(compressed):
        if decompressing:
            decompressed += (compressed[i:i+charlen] * multiplier)
            # move pointer to after all the used chars
            i += charlen
            
            # reset everything
            decompressing = False
            charlen = 0
            multiplier = 0
            prev_loc = -1
        else:
            char = compressed[i]

            if char == '(':
                in_marker = True
                prev_loc = i + 1
            elif char == 'x' and in_marker:
                charlen = int(compressed[prev_loc:i])
                prev_loc = i + 1
            elif char == ')' and in_marker:
                in_marker = False
                decompressing = True
                multiplier = int(compressed[prev_loc:i])
            elif not in_marker:
                decompressed += char
            i += 1
    return decompressed


def find_decompress_data_len(input_file):
    compressed = parse_input(input_file)
    # print(compressed)
    decompressed = decompress_data(compressed)


    # print(decompressed)
    return len(decompressed)

solution = find_decompress_data_len(input_file)

print(f"{solution} is the length of decompressed data")
print(f"Answer is {solution}")
