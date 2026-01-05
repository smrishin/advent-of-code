import hashlib

realinput = ['iwrupvqb']
testinput = ['abcdef', 'pqrstuv']

inputs = realinput

for input in inputs:
    i = 1
    while True:
        key = input + str(i)
        md5_hash = hashlib.md5(key.encode('utf-8'))
        hex_d = md5_hash.hexdigest()
        # if hex_d[:5] == "00000": # Solution for part 1
        if hex_d[:6] == "000000": # solution for part 2
            break
        i += 1
    print(hex_d)
    print(i)