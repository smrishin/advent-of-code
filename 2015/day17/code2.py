
from collections import defaultdict

containers = []
litres_to_store = 150 # 25 #for test input

def parse_input(input_file):
    with open(input_file, 'r') as file:
        for i, line in enumerate(file):
            # print(line.strip())
            containers.append(int(line.strip()))

def container_combinations(input_file):
    parse_input(input_file)
    print(containers)

    combinations = defaultdict(int)
    min_containers_used = float('inf')

    def recur(remain, i, used_containers):
        nonlocal combinations, min_containers_used
        if remain == 0:
            combinations[used_containers] += 1
            min_containers_used = min(min_containers_used, used_containers)
            return
        if remain < 0 or i >= len(containers):
            return 
        
        recur(remain, i + 1, used_containers)
        recur(remain - containers[i], i + 1, used_containers + 1)

    recur(litres_to_store, 0, 0)

    return combinations[min_containers_used], min_containers_used

solution, min_containers_used = container_combinations('input.txt')

print(f"{solution} combinations are possible to fill mininum which is {min_containers_used} containers that can store {litres_to_store} litres of eggnog")
print(f"Answer is {solution}")

