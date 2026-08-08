
input_file = 'input.txt'

def parse_input(input_file):
    triangles = []
    with open(input_file, 'r') as file:
        for line in file:
            # print(line.strip())
            triangles.append(list(map(int,line.strip().split())))
    return triangles

def check_triangle(a, b, c):
    if a+b <= c or a+c <= b or b+c<=a:
        return 0
    return 1

def find_possible_triangles(input_file):
    triangles = parse_input(input_file)
    possible_triangles = 0
    for a, b, c in triangles:
        possible_triangles += check_triangle(a,b,c)
    return possible_triangles

solution = find_possible_triangles(input_file)

print(f"{solution} triangles are possible")
print(f"Answer is {solution}")

