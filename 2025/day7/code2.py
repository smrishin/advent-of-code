from collections import defaultdict

content = []
with open('input.txt', 'r') as file:
    for line in file:
        content.append(line.strip())


beams = {content[0].index("S"):1}

# print(beams)

for level_id in range(1, len(content)):
    if "^" not in content[level_id]:
        continue
    curr = content[level_id]
    next_beams = defaultdict(int)
    for i, count in beams.items():
        if curr[i] == "^":
            next_beams[i-1] += count
            next_beams[i+1] += count
        else:
            next_beams[i] += count

    print(curr)
    beams = next_beams

    print(beams)

print(sum(beams.values()))