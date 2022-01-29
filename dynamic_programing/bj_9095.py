import sys

t = int(sys.stdin.readline().rstrip())

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 11):
    re = 0
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

test_case = [0] * t
for i in range(t):
    temp = int(sys.stdin.readline().rstrip())
    test_case[i] = dp[temp]
for v in test_case:
    print(v)