from typing import List

def count_encoded_chars(s):
    #"" at the start and end will be "\"\"", so +4 to the existing len 
    curr_encoded_count = len(s) + 4 
    i = 1

    while i < len(s) - 1:
        if s[i] == "\\":
            if s[i+1] == "x":
                i += 4
                #\x27 will be \\x27, so +1 to the existing len 
                curr_encoded_count += 1
            else:
                i += 2
                # \" will be \\\", so +2 to the existing len
                # and \\ will be \\\\, so +2 to the existing len
                curr_encoded_count += 2
        else:
            i += 1
    
    return curr_encoded_count


def main():
    strings: List[str] = []

    with open('input.txt', 'r') as file:
        for line in file:
            # print(line.strip())
            strings.append(line.strip())
    encoded_count_total = 0
    memory_count_total = 0

    for s in strings:
        curr_encoded_count = count_encoded_chars(s)
        encoded_count_total += curr_encoded_count
        memory_count_total += len(s)
    # print(memory_count_total, encoded_count_total, encoded_count_total - memory_count_total)

    print(f"number of chars in encoded {encoded_count_total} - number of chars in memory {memory_count_total} = {encoded_count_total - memory_count_total}")



if __name__ == "__main__":
    main()