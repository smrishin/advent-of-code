from typing import List


def turn_on(start: List[int], end: List[int], lights: List[List[bool]]):
    for r in range(start[0], end[0] + 1):
        for c in range(start[1], end[1] + 1):
            lights[r][c] = True

def turn_off(start: List[int], end: List[int], lights: List[List[bool]]):
    for r in range(start[0], end[0] + 1):
        for c in range(start[1], end[1] + 1):
            lights[r][c] = False

def toggle(start: List[int], end: List[int], lights: List[List[bool]]):
    for r in range(start[0], end[0] + 1):
        for c in range(start[1], end[1] + 1):
            lights[r][c] = not lights[r][c]

def count_lights(lights: List[List[bool]]):
    count = 0
    for r in range(1000):
        for c in range(1000):
            if lights[r][c]:
                count += 1
    return count

def main():
    inputs: List[str] = []

    with open('input.txt', 'r') as file:
        for line in file:
            # print(line.strip())
            inputs.append(line.strip())

    lights: List[List[bool]] = [[False] * 1000 for _ in range(1000)]

    for val in inputs:
        parts: List[str] = val.split()

        if len(parts) == 4:
            start = list(map(int, parts[1].split(',')))
            end = list(map(int, parts[3].split(',')))
            toggle(start, end, lights)
        else:
            start = list(map(int, parts[2].split(',')))
            end = list(map(int, parts[4].split(',')))
            if parts[1] == 'on':
                turn_on(start, end, lights)
            else:
                turn_off(start, end, lights)

    print(f"Total lights that are on: {count_lights(lights)}")

if __name__ == "__main__":
    main()