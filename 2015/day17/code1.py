
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

    combinations = 0

    def recur(remain, i):
        nonlocal combinations
        if remain == 0:
            combinations += 1
            return
        if remain < 0 or i >= len(containers):
            return 
        
        recur(remain, i + 1)
        recur(remain - containers[i], i + 1)

    recur(litres_to_store, 0)

    return combinations


solution = container_combinations('input.txt')

print(f"{solution} combinations of containers can store {litres_to_store} litres of eggnog")
print(f"Answer is {solution}")
