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

'''
checks ABA and return BAB or None if its not ABAs
'''
def get_bab(w, i):
    if w[i] != w[i+1] and w[i] == w[i+2]:
        bab = w[i+1] + w[i] + w[i+1]
        return bab
    return None

'''
finds all aba and return a set of corresponding babs
'''
def retrieve_babs_from_outside(word_list):
    babs = set()
    for w in word_list:
        for i in range(len(w) - 2):
            bab = get_bab(w, i)
            if bab:
                babs.add(bab)           
    return babs

def check_inside_for_babs(word_list, babs):
    for w in word_list:
        for i in range(len(w) - 2):
            if w[i] != w[i+1] and w[i] == w[i+2]:
                if w[i:i+3] in babs:
                    return True
    return False

def find_supported_ips(input_file):
    ip_dict = parse_input(input_file)
    supported_ips = 0

    for k, v in ip_dict.items():
        # outside -> v[0], inside -> v[1]
        babs = retrieve_babs_from_outside(v[0])
        if babs and check_inside_for_babs(v[1], babs):
            supported_ips += 1

    return supported_ips

solution = find_supported_ips(input_file)

print(f"{solution} IPs support SSL")
print(f"Answer is {solution}")
