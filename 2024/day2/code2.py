reports = []

with open('input.txt', 'r') as file:
    for line in file:
        # print(line.strip())
        level = line.strip().split(" ")
        level = list(map(int, level))
        reports.append(level)
    
def isIncreasing(arr):
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        if not (1 <= diff <= 3):
            return False
    return True

def isDecreasing(arr):
    for i in range(1, len(arr)):
        diff = arr[i - 1] - arr[i]
        if not (1 <= diff <= 3):
            return False
    return True

def checkReportSafety(arr):
    n = len(arr)
    
    if isIncreasing(arr) or isDecreasing(arr):
        return True
    
    for i in range(n):
        new_arr = arr[:i] + arr[i + 1:]
        if isIncreasing(new_arr) or isDecreasing(new_arr):
            return True
    
    return False


safeCount = 0

for r in reports:
    if checkReportSafety(r):
        # print(r)
        safeCount += 1

print(f"{safeCount} reports are safe")