# acmicpc.net/problem/2193

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (91)
endZero = [0] * (91)

dp[1] = 1 # 1
endZero[1] = 0
dp[2] = 1 # 10
endZero[2] = 1
dp[3] = 2 # 100, 101
endZero[3] = 1

for i in range(4, n+1):
    beforeEndOne = dp[i-1] - endZero[i-1]
    dp[i] = beforeEndOne + endZero[i-1] * 2
    endZero[i] = endZero[i-1] + beforeEndOne

print(dp[n])