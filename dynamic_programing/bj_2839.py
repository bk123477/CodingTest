import sys

n = int(sys.stdin.readline().rstrip())
dp = [-1] * (5001)
dp[3] = 1
dp[5] = 1
# n은 3~5000범위
for i in range(5, n+1):
    a, b = 0, 0
    if dp[i-3] == -1 and dp[i-5] == -1: # 3과 5로 만들 수 없는 수
        continue
    else: # 3과 5로 만들 수 있는 수
        if dp[i - 3] != -1:
            a = dp[i-3]
        else:
            a = 5001
        if dp[i - 5] != -1:
            b = dp[i-5]
        else:
            b = 5001
        
    dp[i] = min(a, b) + 1
print(dp[n])
