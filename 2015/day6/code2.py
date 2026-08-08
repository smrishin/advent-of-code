from typing import List

def turn_on(start: List[int], end: List[int], lights: List[List[int]]):
    for r in range(start[0], end[0] + 1):
        for c in range(start[1], end[1] + 1):
            lights[r][c] += 1

def turn_off(start: List[int], end: List[int], lights: List[List[int]]):
    for r in range(start[0], end[0] + 1):
        for c in range(start[1], end[1] + 1):
            if lights[r][c] > 0:
                lights[r][c] -= 1

def toggle(start: List[int], end: List[int], lights: List[List[int]]):
    for r in range(start[0], end[0] + 1):
        for c in range(start[1], end[1] + 1):
            lights[r][c] += 2

def count_brightness(lights: List[List[int]]):
    brightness = 0
    for r in range(1000):
        for c in range(1000):
            brightness += lights[r][c]
    return brightness

def main():
    inputs: List[str] = []

    with open('input.txt', 'r') as file:
        for line in file:
            # print(line.strip())
            inputs.append(line.strip())

    lights: List[List[int]] = [[0] * 1000 for _ in range(1000)]

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

    print(f"Total brightness of all lights is {count_brightness(lights)}")

if __name__ == "__main__":
    main()