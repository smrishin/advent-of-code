from collections import defaultdict, deque

input_file = 'input.txt'
chips_to_compare = [61, 17] #[2, 5]

def parse_input(input_file):
    ''' bots schema
    bots = {
        id: [chips]
        0 : [2, 5],
        1 : [10, 3]
    }
    '''
    bots = defaultdict(list)
    ''' instructions schema
    instructions = {
        bot_id: [
            [
            "low",
            "type", #"bot"
            id  #bot_id
            ],
            [
            "high",
            "type", #"output"
            id #out_id
            ]
        ]
    }
    '''
    instructions = defaultdict(list)

    bots_with_2_chips = deque()

    with open(input_file, 'r') as file:
        for line in file:
            # print(line.strip())
            parts = line.strip().split()
            if parts[0] == "value":
                bot_id = int(parts[-1])
                chip_id = int(parts[1])
                bots[bot_id].append(chip_id)
                if len(bots[bot_id]) == 2:
                    bots_with_2_chips.append(bot_id)
            if parts[0] == "bot":
                bot_id = int(parts[1])
                low = ["low", parts[5], int(parts[6])]
                hi = ["hi", parts[-2], int(parts[-1])]
                instructions[bot_id].append(low)
                instructions[bot_id].append(hi)
    return bots, instructions, bots_with_2_chips

def check_if_chips_to_compare_exist(bot_chips):
    return bot_chips[0] in chips_to_compare and bot_chips[1] in chips_to_compare

def process_bot_instructions(input_file):
    bots, instructions, bots_with_2_chips = parse_input(input_file)
    output = defaultdict(int)
    # print(instructions)
    processed_bots = []
    part1 = -1
    while bots_with_2_chips:
        bot_id = bots_with_2_chips.popleft()
        if check_if_chips_to_compare_exist(bots[bot_id]):
            part1 = bot_id

        processed_bots.append(bot_id)
        ins = instructions[bot_id]
        curr_chips = bots[bot_id]
        # process low
        if ins[0][1] == "output":
            output[ins[0][2]] = min(curr_chips)
        else:
            bots[ins[0][2]].append(min(curr_chips))
            if len(bots[ins[0][2]]) == 2:
                bots_with_2_chips.append(ins[0][2])

        # process hi
        if ins[1][1] == "output":
            output[ins[1][2]] = max(curr_chips)
        else:
            bots[ins[1][2]].append(max(curr_chips))
            if len(bots[ins[1][2]]) == 2:
                bots_with_2_chips.append(ins[1][2])

    # print(max(processed_bots))
    # print(len(processed_bots))
    # print(output)
    part2 = output[0] * output[1] * output[2]
    return part1, part2

solution1, solution2 = process_bot_instructions(input_file)

print(f"Part 1 : Bot {solution1} compares chip {chips_to_compare[0]} with chip {chips_to_compare[1]}")
print(f"Answer is {solution1} \n")
print(f"Part 2 : {solution2} is the product of chips in output 0,1,2")
print(f"Answer is {solution2}")
