from collections import defaultdict
import re

input_file = 'input.txt'

def parse_input(input_file):
    ip_dict = defaultdict(list)
    with open(input_file, 'r') as file:
        for idx, line in enumerate(file):
            # print(line.strip())
            outside = [val.strip()
                       for val in re.split(r"\[.*?\]", line.strip())
                       if val.strip()]
            inside = re.findall(r"\[(.*?)\]", line.strip())

            ip_dict[idx] = [outside, inside]
    return ip_dict

def check_abba(w, i):
        return w[i] != w[i+1] and w[i] == w[i+3] and w[i+1] == w[i+2]

def find_abba(word_list):
    for w in word_list:
        for i in range(len(w) - 3):
            if check_abba(w, i):
                return True
    return False

def find_supported_ips(input_file):
    ip_dict = parse_input(input_file)
    supported_ips = 0
    for k, v in ip_dict.items():
        # outside -> v[0], inside -> v[1]
        if find_abba(v[0]) and not find_abba(v[1]):
            supported_ips += 1
        # print(k, outside_valid and inside_valid)
    return supported_ips

solution = find_supported_ips(input_file)

print(f"{solution} IPs support TLS")
print(f"Answer is {solution}")
