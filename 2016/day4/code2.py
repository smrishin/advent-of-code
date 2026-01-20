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
            encrypted_name = "-".join(parts[:-1])
            sector_id = int(parts[-1])

            data.append((encrypted_name, sector_id, checksum))
    return data

def check_real_room(enc, checksum):
    count = Counter(enc)
    del count["-"]
    heap = []
    for k, v in count.items():
        heappush(heap, (-v, k))
    code = ""
    while heap and len(code) < 5:
        code += heappop(heap)[1]
    # print(code)
    return code == checksum

def find_real_rooms(data):
    real_rooms = []
    for enc, sid, checksum in data:
        if check_real_room(enc, checksum):
            real_rooms.append((enc, sid))
    return real_rooms

def find_decrypted_letter(c, sid):
    char_loc = ord('a') + ((ord(c) - ord('a')) + sid) % 26
    return chr(char_loc)

def decrypt_name(enc, sid):
    words = []
    word = ""
    for c in enc:
        if c == "-":
            words.append(word)
            word = ""
            continue
        word += find_decrypted_letter(c, sid)
    # add the last word
    words.append(word)

    return " ".join(words)

def find_northpole_objects_sector_id(input_file):
    data = parse_input(input_file)
    real_rooms = find_real_rooms(data)
    # print(real_rooms)
    decrypted_names = []

    for enc, sid in real_rooms:
        decryted_name = decrypt_name(enc, sid)
        decrypted_names.append((decryted_name, sid))
    # print(decrypted_names)

    for decryted_name, sid in decrypted_names:
        if 'north' in decryted_name:
            print(f"Decryted Name: {decryted_name} \nSector Id: {sid}")
            return sid
    return 0

solution = find_northpole_objects_sector_id(input_file)

print(f"{solution} is the sector id where North Pole Objects are stored")
print(f"Answer is {solution}")

