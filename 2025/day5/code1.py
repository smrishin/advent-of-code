rangeStrs = []
ingredientsStr = []

with open('input.txt', 'r') as file:
    content = file.read().split("\n")
    indexof = content.index("")
    rangeStrs = content[:indexof]
    ingredientsStr = content[indexof + 1:]

ingredients = [int(i) for i in ingredientsStr]

def sortAndMergeRanges(rangeStrs):
    intervals = []
    for r in rangeStrs:
        a,b = r.split("-")
        intervals.append([int(a),int(b)])

    intervals.sort()

    merged = []

    for i in intervals:
        if len(merged) == 0 or merged[-1][1] < i[0]:
            merged.append(i)
        else:
            merged[-1][1] = max(merged[-1][1], i[1])
    return merged

def checkFreshness(id):
    for a, b in ranges:
        if a <= id <= b:
            return True
        
    return False

ranges = sortAndMergeRanges(rangeStrs)

freshCount = 0
for i in ingredients:
    if checkFreshness(i):
        freshCount += 1

print(f"fresh ingredients count is {freshCount}")


        
    