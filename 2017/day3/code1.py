
puzzle_input = 289326 #1024

def binary_search(start, end, target):
    l = 0
    r = end - start

    while l <= r:
        m = (l + r)//2
        if start + m == target:
            return m
        elif target < start + m:
            r = m - 1
        else:
            l = m


def find_steps(num):
    i = 1
    ring = 0
    while i**2 < num:
        i += 2
        ring +=1
    # highest val in the ring, bottom right
    high = i**2
    # lowest val of the ring in this below val +1
    low = (i-2)**2
    # mid val of the ring is this below val +1
    mid = (i-1)**2
    top_right = (low + 1 + mid) // 2
    bottom_left = (mid + 1 + high) // 2

    # case1 c = ring, r = ?
    if low < num <= top_right:
        c = ring
        # binary search to get r
        r_i = binary_search(low + 1, top_right, num) + 1
        r = abs(r_i - (i//2))

    # case2 r = ring, c = ?
    elif top_right < num <= mid:
        r = ring
        # binary search to get c
        c_i = binary_search(top_right + 1, mid+1, num) + 1
        c = abs(c_i - (i//2))

    # case3 r = ring, c = ?
    elif mid < num <= bottom_left:
        r = ring
        # binary search to get c
        c_i = binary_search(mid + 2, bottom_left, num) + 1
        c = abs(c_i - (i//2))

    # case4 c = ring, r = ?
    else:
        c = ring
        # binary search to get r
        r_i = binary_search(bottom_left + 1, high, num) + 1
        r = abs(r_i - (i//2))    

    return r + c

solution = find_steps(puzzle_input)

print(f"No. of steps to the center is {solution}")
print(f"Answer is {solution}")

