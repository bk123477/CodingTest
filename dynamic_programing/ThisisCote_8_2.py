

import sys
input = sys.stdin.readline
INF = 1e9

x = int(input().rstrip())
dp = [0 for _ in range(x+1)] # 0 ~ x까지 0으로 초기화
dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 1
for i in range(6, x+1):
    t1 = t2 = t3 = t4 = INF
    if i % 5 == 0:
        t1 = dp[i // 5] + 1
    if i % 3 == 0:
        t2 = dp[i // 3] + 1
    if i % 2 == 0:
        t3 = dp[i // 2] + 1
    t4 = dp[i - 1] + 1
    dp[i] = min(t1, t2, t3, t4)

print(dp[x])
print(dp)