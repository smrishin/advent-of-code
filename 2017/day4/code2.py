input_file = 'input.txt'

from collections import defaultdict

def parse_input(input_file):
    passphrases = []
    with open(input_file, 'r') as file:
        for line in file:
            # print(line.strip())
            row = line.strip().split()
            passphrases.append(row)
    return passphrases

def create_anagram_code(word):
    code = [0] * 26
    for i in word:
        code[ord(i) - ord('a')] += 1
    # print(word, code, ' '.join(code))
    return tuple(code)

def check_anagrams_exist(words):
    anagrams = set()
    for word in words:
        code = create_anagram_code(word)
        if code in anagrams:
            return True
        anagrams.add(code)
    return False

def check_non_anagram_words(input_file):
    passphrases = parse_input(input_file)
    res = 0

    for words in passphrases:
        res += 0 if check_anagrams_exist(words) else 1


    return res

solution = check_non_anagram_words(input_file)

print(f"Number of paraphrases without anagrams are {solution}")
print(f"Answer is {solution}")

