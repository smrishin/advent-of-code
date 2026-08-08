from collections import defaultdict
input_file = 'input.txt'

def parse_input(input_file):
    triangles_dict = defaultdict(list)
    with open(input_file, 'r') as file:
        for line in file:
            # print(line.strip())
            curr_triangles = (list(map(int,line.strip().split())))
            for i, val in enumerate(curr_triangles):
                triangles_dict[i].append(val)
    triangles = []
    for k, v in triangles_dict.items():
        triangles += v
    return triangles

def check_triangle(a, b, c):
    if a+b <= c or a+c <= b or b+c<=a:
        return 0
    return 1

def find_possible_triangles(input_file):
    triangles = parse_input(input_file)
    possible_triangles = 0
    for i in range(0, len(triangles), 3):
        if i + 2 >= len(triangles):
            break
        a = triangles[i]
        b = triangles[i + 1]
        c = triangles[i + 2]
        possible_triangles += check_triangle(a,b,c)
    return possible_triangles

solution = find_possible_triangles(input_file)

print(f"{solution} triangles are possible")
print(f"Answer is {solution}")

