from typing import List

def count_chars(s):
    curr_string_count = 0
    i = 1

    while i < len(s) - 1:
        if s[i] == "\\":
            if s[i+1] == "x":
                i += 4
            else:
                i += 2
        else:
            i += 1
        curr_string_count += 1
    
    return curr_string_count


def main():
    strings: List[str] = []

    with open('input.txt', 'r') as file:
        for line in file:
            # print(line.strip())
            strings.append(line.strip())
    string_count_total = 0
    memory_count_total = 0

    for s in strings:
        curr_string_count = count_chars(s)
        string_count_total += curr_string_count
        memory_count_total += len(s)
    # print(memory_count_total, string_count_total, memory_count_total - string_count_total)

    print(f"number of chars in memory {memory_count_total} - number of chars in string {string_count_total} = {memory_count_total - string_count_total}")



if __name__ == "__main__":
    main()