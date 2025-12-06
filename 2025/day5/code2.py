rangeStrs = []

with open('input.txt', 'r') as file:
    content = file.read().split("\n")
    indexof = content.index("")
    rangeStrs = content[:indexof]

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

ranges = sortAndMergeRanges(rangeStrs)
totalCount = 0

for a,b in ranges:
    totalCount += b-a+1

print(f"ingredient IDs count {totalCount}")


        
    