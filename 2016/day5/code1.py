import hashlib

puzzle_input = 'cxdnnyjw' #'abc'
length_of_password = 8

def find_password(puzzle_input):
    password = ""
    i = 0
    while len(password) < length_of_password:
        key = puzzle_input + str(i)
        md5_hash = hashlib.md5(key.encode('utf-8'))
        hex_d = md5_hash.hexdigest()
        if hex_d[:5] == "00000":
            password += hex_d[5]
        # if hex_d[:6] == "000000": # solution for part 2
        #     break
        i += 1
    return password
solution = find_password(puzzle_input)

print(f"{solution} is the password")
print(f"Answer is {solution}")

