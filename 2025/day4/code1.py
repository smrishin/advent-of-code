grid = []

with open('input.txt', 'r') as file:
    for line in file:
        # print(line.strip())
        grid.append(list(line.strip()))

for row in grid:
    print(row, "\n")

R = len(grid)
C = len(grid[0])
directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
res = 0

for r in range(R):
    for c in range(C):
        if grid[r][c] == ".":
            continue

        count = 0
        for ro, co in directions:
            nr, nc = r + ro, c + co
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == "@":
                count += 1
                if count > 3:
                    break
        if count > 3:
            continue
        else:
            res += 1


print(res)