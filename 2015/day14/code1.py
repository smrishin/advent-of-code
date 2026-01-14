reindeers = set()
details = dict()
for line in open('input.txt'):
    parts = line.split()

    name = parts[0]
    speed = int(parts[3])
    travel_time = int(parts[6])
    rest_time = int(parts[-2])

    reindeers.add(name)

    details[name] = {
        "speed" : speed,
        "travel_time": travel_time,
        "rest_time": rest_time,
        "cycle_time": travel_time + rest_time,
        "cycle_distance": speed * travel_time
    }

# for k, v in details.items():
#     print(k, v)

distances = []
for deer in reindeers:
    cycles = 2503 // details[deer]["cycle_time"]
    remainder = 2503 % details[deer]["cycle_time"]
    # print(cycles, remainder)
    if remainder >= details[deer]["travel_time"]:
        distances.append((cycles+1) * details[deer]["cycle_distance"])
    else:
        distances.append((cycles * details[deer]["cycle_distance"]) + (remainder * details[deer]["speed"]))
    
print(max(distances))