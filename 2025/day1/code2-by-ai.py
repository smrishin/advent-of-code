res = 0
curr = 50

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        direction = line[0]       # 'L' or 'R'
        steps = int(line[1:])

        if direction == "R":
            # You visit curr+1, curr+2, ..., curr+steps
            start_excl = curr
            end_incl = curr + steps

            hits = end_incl // 100 - start_excl // 100
            curr = end_incl

        else:  # direction == 'L'
            # You visit curr-1, curr-2, ..., curr-steps
            start_incl = curr - steps
            end_excl = curr

            # Multiples of 100 in [start_incl, end_excl)
            hits = (end_excl - 1) // 100 - (start_incl - 1) // 100
            curr = start_incl

        res += hits
        print(line, curr % 100, res, "\n")

print(res)
