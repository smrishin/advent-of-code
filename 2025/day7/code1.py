content = []
with open('input.txt', 'r') as file:
    for line in file:
        content.append(line.strip())


beam_locations = set()

entry = content[0].index("S")

beam_locations.add(entry)
# print(beam_locations)
res = 0

for level_id in range(1, len(content)):
    if "^" not in content[level_id]:
        continue
    curr = content[level_id]
    for i in range(len(curr)):
        if curr[i] == "^" and i in beam_locations:
            res += 1
            beam_locations.remove(i)
            beam_locations.add(i-1)
            beam_locations.add(i+1)


print(res)