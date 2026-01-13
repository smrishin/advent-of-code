from typing import List, Dict

realinput = "cqjxjnds"
testinput = "abcdefgh"

def inc(letter):
    if letter == "z":
        return "a"
    return chr(ord(letter) + 1)


def increment(password):    
    n = len(password)
    pass_arr = list(password)
    for i in range(n - 1, -1, -1):
        pass_arr[i] = inc(pass_arr[i])
        if pass_arr[i] != "a":
            break
    return "".join(pass_arr)

def check_increasing_straight(password):
    for a, b, c in zip(password[:-2], password[1:-1], password[2:]):
        if ord(a) == ord(b) - 1 == ord(c) - 2:
            return True
    return False

    # i = 0
    # n = len(password)
    # while i < n - 2:
    #     if ord(password[i]) == ord(password[i + 1]) - 1 == ord(password[i + 2]) - 2:
    #         return True
    #     i += 1
    # return False
        

def check_iol(password):
    pass_arr = list(password)

    def find_index(arr, val):
        try:
            return arr.index(val)
        except ValueError:
            return float("inf")
        

    i_pos = find_index(pass_arr, "i")
    o_pos = find_index(pass_arr, "o")
    l_pos = find_index(pass_arr, "l")

    min_pos = min(i_pos, o_pos, l_pos)

    if min_pos == float("inf"):
        return password

    pass_arr[min_pos] = inc(pass_arr[min_pos])

    for i in range(min_pos + 1, len(pass_arr)):
        pass_arr[i] = "a"

    return "".join(pass_arr)




def check_pairs(password):
    pair_sets = set()
    i = 0

    while i < len(password) - 1:
        if password[i] == password[i+1]:
            pair_sets.add(password[i])
            i += 1
        i += 1
    return len(pair_sets) >= 2

def find_new_password(password):
    if len(password) > 8:
        return "PASSWORD TOO LONG TO START WITH"
    timeout_count = 0
    while True:
        if timeout_count > 1000000:
            return "LOOP TAKING TOO LONG"
        timeout_count += 1

        password = increment(password)
        password = check_iol(password)
        condition3 = check_pairs(password)
        condition1 = check_increasing_straight(password)

        if condition1 and condition3:
            print(timeout_count)
            return password
        
    

def main():
    password = realinput

    # Part 1
    password = find_new_password(password)
    print(f"Santa's password after first expiry is : {password}")

    # Part 2
    password = find_new_password(password)
    print(f"Santa's password after second expiry is : {password}")



if __name__ == "__main__":
    main()