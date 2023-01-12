# 간단한건데 못풂.. 예전엔 풀었느데..

import sys
input = sys.stdin.readline

n = int(input().rstrip()) # 가로 N * 세로 2인 바닥
dp = [0 for _ in range(n+1)]

dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] = (dp[i-1] + 2*dp[i-2]) % 796796

print(dp[n])