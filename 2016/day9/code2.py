'''
solved with the help of 
https://www.reddit.com/r/adventofcode/comments/5hbygy/comment/daz279z/
'''

input_file = 'input.txt'

def parse_input(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            # print(line.strip())
            return line.strip()

def decompress_data(compressed):
    if '(' not in compressed:
        return len(compressed)
    
    decompressed_len = 0

    while '(' in compressed:
        marker_start = compressed.find('(')
        decompressed_len += marker_start #because until the marker start, the len is same as compressed
        compressed = compressed[marker_start:]
        marker_end = compressed.find(')')
        charlen, multiplier = map(int,compressed[1:marker_end].split('x'))
        compressed = compressed[marker_end + 1:]
        
        decompressed_len += decompress_data(compressed[:charlen]) * multiplier

        compressed = compressed[charlen:]
    decompressed_len += len(compressed)
    return decompressed_len

def find_decompress_data_len(input_file):
    compressed = parse_input(input_file)
    # print(compressed)
    
    return decompress_data(compressed)

solution = find_decompress_data_len(input_file)

print(f"{solution} is the length of decompressed data")
print(f"Answer is {solution}")
