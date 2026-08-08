
input_file = 'input.txt'

def parse_input(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            # print(line.strip())
            seq = line.strip()
    return seq

def digit_sum(n):
    res = int(n[-1]) if n[-1] == n[0] else 0
    for i, j in zip(n[:-1], n[1:]):
        if i == j:
            res += int(i)

    return res

def solve_captcha(input_file):
    seq = parse_input(input_file)
    seq_sum = digit_sum(seq)

    return seq_sum

solution = solve_captcha(input_file)

print(f"Sum of the sequence is {solution}")
print(f"Answer is {solution}")

