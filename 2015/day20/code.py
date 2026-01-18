# For the actual input it takes forever, need optimization

puzzle_input = 150 #29000000

def get_divisors(n):
    divisors = set()

    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
        i += 1
    # print(divisors)
    return sorted(divisors)

def calculate_presents(divs):
    total = 0

    for d in divs:
        total += d*10

    return total

def elves_deliver_presents():
    for i in range(1, 1 + (puzzle_input//10)):        
        divs = get_divisors(i)
        no_of_presents = calculate_presents(divs)
        if no_of_presents >= puzzle_input:
            return i



solution = elves_deliver_presents() 

print(f"{solution} is the lowest house number to have min {puzzle_input} presents")
print(f"Answer is {solution}")
