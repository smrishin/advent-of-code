reindeers = set()
details = []
for line in open('input.txt'):
    parts = line.split()

    name = parts[0]
    speed = int(parts[3])
    travel_time = int(parts[6])
    rest_time = int(parts[-2])

    reindeers.add(name)

    details.append({
        "score": 0,
        "curr_distance": 0,
        "name": name,
        "speed" : speed,
        "travel_time": travel_time,
        "rest_time": rest_time,
        "cycle_time": travel_time + rest_time,
        "cycle_distance": speed * travel_time
    })
TIME_LIMIT = 2503 #1000
for i in range(1, TIME_LIMIT + 1):
    curr_distances = []
    for deer in details:
        cycle_number = i % deer["cycle_time"]
        resting = bool(cycle_number == 0 or cycle_number > deer['travel_time'])
        if not resting:
            deer["curr_distance"] += deer["speed"]
        curr_distances.append(deer["curr_distance"])

    max_dist = max(curr_distances)

    for deer in details:
        if deer["curr_distance"] == max_dist:
            deer["score"] += 1

max_score = 0
max_scorer = ""
max_scorer_distance = 0
print("Name\t", "Score\t", "Distance")
for d in details:
    if d["score"] > max_score:
        max_score = d["score"]
        max_scorer = d["name"]
        max_scorer_distance = d["curr_distance"]
    print(f"{d['name']}\t {d['score']}\t {d['curr_distance']}")

print(f"The winner of the competition is {max_scorer} with {max_score} points and {max_scorer_distance} km in {TIME_LIMIT} seconds")


