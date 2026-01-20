from collections import defaultdict, Counter
input_file = 'input.txt'

def parse_input(input_file):
    message_dict = defaultdict(list)
    with open(input_file, 'r') as file:
        for line in file:
            # print(line.strip())
            curr_message = (list(line.strip()))
            for i, val in enumerate(curr_message):
                message_dict[i].append(val)
    return message_dict

# part1
def most_common_char(char):
    count = Counter(char)
    max_count = max(count.values())

    for k,v in count.items():
        if v == max_count:
            return k

# part2
def least_common_char(char):
    count = Counter(char)
    min_count = min(count.values())

    for k,v in count.items():
        if v == min_count:
            return k


def error_correct_message(input_file):
    message_dict = parse_input(input_file)
    message_part1 = ""
    message_part2 = ""
    for _, v in message_dict.items():
        message_part1 += most_common_char(v)
        message_part2 += least_common_char(v)
    return message_part1, message_part2

solution1, solution2 = error_correct_message(input_file)

print(f"Part1 {solution1} is the error corrected message")
print(f"Answer is {solution1}")

print(f"Part2 {solution1} is the error corrected message")
print(f"Answer is {solution2}")
