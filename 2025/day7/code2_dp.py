from functools import lru_cache

content = []
with open('input.txt', 'r') as file:
    for line in file:
        content.append(line.strip())


entry = content[0].index("S")
lines = [line for line in content if "^" in line]
# print(lines)

n = len(lines)
m = len(lines[0])

'''
DP Top Down
'''

memo = {}

# @lru_cache(None)
def dp_td(i, pos):
    if i == n:
        return 1
    
    if (i, pos) in memo:
        return memo[(i,pos)]    
    
    if lines[i][pos] == "^":
        memo[(i,pos)] = dp_td(i + 1, pos + 1) + dp_td(i + 1, pos - 1)
    else:
        memo[(i,pos)] = dp_td(i + 1, pos)

    return memo[(i,pos)]

dp_topdown_res = dp_td(0, entry)

print(f"Results using Top Down DP: {dp_topdown_res} timelines")

'''
DP Bottom up
'''

# dp[i][pos] where i is the curr level, pos is the position of the beam

def dp_bu():
    dp = [[0] * m for _ in range(n + 1)]

    for pos in range(m):
        dp[n][pos] = 1

    for i in range(n-1, -1, -1):
        for pos in range(m):
            if lines[i][pos] == "^":
                if pos - 1>=0:
                    dp[i][pos] += dp[i + 1][pos - 1]
                if pos + 1 < m:
                    dp[i][pos] += dp[i + 1][pos + 1]
            else:
                dp[i][pos] += dp[i + 1][pos]
    
    return dp[0][entry]
    
dp_bottomup_res = dp_bu()

print(f"Result using Bottom up DP: {dp_bottomup_res} timelines")