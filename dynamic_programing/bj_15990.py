import sys


dp = [[0 for _ in range(3)] for _ in range(100001)]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]
for i in range(4, 100001):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 1000000009
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % 1000000009
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % 1000000009

t = int(sys.stdin.readline().rstrip())
for i in range(t):
    temp = int(sys.stdin.readline().rstrip())
    print(sum(dp[temp])%1000000009)