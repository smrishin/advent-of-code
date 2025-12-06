reports = []

with open('input.txt', 'r') as file:
    for line in file:
        # print(line.strip())
        level = line.strip().split(" ")
        level = list(map(int, level))
        reports.append(level)
    
def checkIsDecreasing(num: int) -> bool:
    return True if num > 0 else False

def checkReportSafety(report):    
    isDecreasing = checkIsDecreasing(report[0] - report[1])

    for i in range(len(report)-1):
        diff = report[i] - report[i+1]
        if checkIsDecreasing(diff) == isDecreasing and 1 <= abs(diff) <= 3:
            continue
        else:
            return False
    return True


safeCount = 0

for r in reports:
    if checkReportSafety(r):
        # print(r)
        safeCount += 1

print(f"{safeCount} reports are safe")