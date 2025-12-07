grid = []
with open('input.txt', 'r') as file:
    for line in file:
        # print(line.strip())
        grid.append(list(line.strip()))

# for r in grid:
#     print(r)

R = len(grid)
C = len(grid[0])
directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
res = 0

def check_pos_and_char(nr, nc, char):
    return 0<=nr<R and 0<=nc<C and grid[nr][nc] == char

for r in range(R):
    for c in range(C):
        if grid[r][c] == "X":
            for ro, co in directions:
                rM, cM = r + ro, c + co
                rA, cA = r + ro*2, c + co*2
                rS, cS = r + ro*3, c + co*3
                if (
                    check_pos_and_char(rM, cM, "M") and 
                    check_pos_and_char(rA, cA, "A") and 
                    check_pos_and_char(rS, cS, "S")
                    ):
                    res += 1

print(f"The word XMAS appears {res} times")
