import hashlib
import sys

puzzle_input = 'cxdnnyjw' #'abc'
length_of_password = 8

def find_password(puzzle_input):
    password = ["-"] * 8
    pass_len = 0
    i = 0
    while pass_len < length_of_password:
        key = puzzle_input + str(i)
        md5_hash = hashlib.md5(key.encode('utf-8'))
        hex_d = md5_hash.hexdigest()
        if hex_d[:5] == "00000":
            pos = int(hex_d[5], 16)
            if pos < 8 and password[pos] == '-':
                pass_len += 1
                password[pos] = hex_d[6]
        i += 1
        '''
        the next if statement is the "cinematic decrypting animation" as optional part of the question
        this statement is stolen from a reddit comment
        https://www.reddit.com/r/adventofcode/comments/5gk2yv/comment/dat36do/ 
        '''
        if i % 1000 == 0:
            sys.stdout.write("password: {} cracking hash: {} \r".format("".join(password),hex_d))
            sys.stdout.flush()

    return "".join(password)

solution = find_password(puzzle_input)

print(f"\n{solution} is the password")
print(f"Answer is {solution}")

