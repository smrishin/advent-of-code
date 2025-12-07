grid = []
with open('input.txt', 'r') as file:
    for line in file:
        # print(line.strip())
        grid.append(list(line.strip()))

# for r in grid:
#     print(r)

R = len(grid)
C = len(grid[0])
res = 0

def check_pos_and_char(nr, nc, char):
    return 0<=nr<R and 0<=nc<C and grid[nr][nc] == char

for r in range(R):
    for c in range(C):
        if grid[r][c] == "A":
            # pos dia
            par, pac = r + 1, c + 1
            pbr, pbc = r - 1, c - 1

            # neg dia
            nar, nac = r + 1, c - 1
            nbr, nbc = r - 1, c + 1

            if (
                # pos diagonal
                ((check_pos_and_char(par, pac, "M") and check_pos_and_char(pbr, pbc, "S")) or 
                (check_pos_and_char(par, pac, "S") and check_pos_and_char(pbr, pbc, "M"))) and
                # neg diagonal
                ((check_pos_and_char(nar, nac, "M") and check_pos_and_char(nbr, nbc, "S")) or 
                (check_pos_and_char(nar, nac, "S") and check_pos_and_char(nbr, nbc, "M")))
                ):
                res += 1

print(f"two MAS in the shape of an X appears {res} times")
