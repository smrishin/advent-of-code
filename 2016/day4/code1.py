from collections import Counter
from heapq import heappush, heappop

input_file = 'input.txt'

def parse_input(input_file):
    data = [] #(encrypted name, sectorId, checksum)
    with open(input_file, 'r') as file:
        for line in file:
            # print(line.strip())
            left, right = line.strip().split("[")
            checksum = right[:-1]
            
            parts = left.split("-")
            encrypted_name = "".join(parts[:-1])
            sector_id = int(parts[-1])

            data.append((encrypted_name, sector_id, checksum))
    return data

def check_real_room(enc, checksum):
    count = Counter(enc)
    heap = []
    for k, v in count.items():
        heappush(heap, (-v, k))
    code = ""
    while heap and len(code) < 5:
        code += heappop(heap)[1]
    return code == checksum

def find_real_room_ids(input_file):
    data = parse_input(input_file)
    sector_id_sum = 0
    for enc, sid, checksum in data:
        if check_real_room(enc, checksum):
            sector_id_sum += sid
    return sector_id_sum

solution = find_real_room_ids(input_file)

print(f"{solution} are real rooms")
print(f"Answer is {solution}")

