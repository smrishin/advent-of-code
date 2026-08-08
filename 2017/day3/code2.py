puzzle_input = 289326

def first_value_larger_than(target: int) -> int:
    grid = {(0, 0): 1}

    # right, up, left, down
    directions = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
    ]

    x = y = 0
    step_length = 1
    direction_index = 0

    while True:
        # Move the same distance in two directions,
        # then increase the distance.
        for _ in range(2):
            dx, dy = directions[direction_index % 4]

            for _ in range(step_length):
                x += dx
                y += dy

                value = sum(
                    grid.get((x + nx, y + ny), 0)
                    for nx in (-1, 0, 1)
                    for ny in (-1, 0, 1)
                    if not (nx == 0 and ny == 0)
                )

                if value > target:
                    return value

                grid[(x, y)] = value

            direction_index += 1

        step_length += 1


print(first_value_larger_than(puzzle_input))