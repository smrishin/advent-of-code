from typing import List

ingredients: List[dict] = []
max_score = 0

def parse_input(input_file):
    with open(input_file, 'r') as file:
        for i, line in enumerate(file):
            # print(line.strip())
            parts = line.split()
            ingredient = {
                "id": i,
                "name": parts[0][:-1],
                "capacity": int(parts[2][:-1]),
                "durability": int(parts[4][:-1]),
                "flavor": int(parts[6][:-1]),
                "texture": int(parts[8][:-1]),
                "calories": int(parts[10])
            }
            ingredients.append(ingredient)

def score_cookie(quantity):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    for i, item in enumerate(ingredients):
        capacity += quantity[i] * item["capacity"]
        durability += quantity[i] * item["durability"]
        flavor += quantity[i] * item["flavor"]
        texture += quantity[i] * item["texture"]

    capacity = capacity if capacity > 0 else 0 
    durability = durability if durability > 0 else 0 
    flavor = flavor if flavor > 0 else 0 
    texture = texture if texture > 0 else 0 

    return capacity * durability * flavor * texture

def make_cookies(remaining, total, quantity = []):
    global max_score
    for i in range(1, remaining + 1):
        quantity.append(i)

        # if only 1 ingredient in remaining then just add it to the the quantity instead of sending to another recursive call
        if len(quantity) == len(ingredients) - 1: 
            quantity.append(remaining - i)
            curr_cookie_score = score_cookie(quantity)
            if curr_cookie_score > max_score:
                max_score = curr_cookie_score
            quantity.pop() #pop the final ingredient here cuz you added it here.
        else:
            make_cookies(remaining - i, total, quantity)
        quantity.pop()


def top_score_cookie(input_file, teaspoon_limits):
    parse_input(input_file)
    for i in ingredients:
        print(i)

    make_cookies(teaspoon_limits, teaspoon_limits)
    print(f"Best cookie score is {max_score}")

    return max_score


solution = top_score_cookie('input.txt', 100)

print(f"Best cookie score is {solution}")

