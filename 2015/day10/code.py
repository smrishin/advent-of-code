from typing import List

realinput = "3113322113"
testinput = "1"

def recur(curr, count_down):
    if count_down == 0:
        return curr

    n = len(curr)

    if n == 1:
        return recur("1" + curr, count_down - 1)
    
    digit = curr[0]
    res = ""
    l = 0
    r = 0

    while r < n:
        if curr[r] == digit:
            r += 1
        else:
            res += str(r - l) + digit
            l = r
            digit = curr[l]
    res += str(r-l) + curr[-1]

    return recur(res, count_down - 1)

def main():
    curr = realinput #testinput
    # 40 for part 1, 50 for part 2, 5 for testinput
    # for _ in range(50): 
    res = recur(curr, 50)
    print(f"{len(res)} is the len of the output after look and say")


if __name__ == "__main__":
    main()