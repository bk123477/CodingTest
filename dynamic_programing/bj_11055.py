import sys

n = int(sys.stdin.readline().rstrip())
li = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [0] * n
for i in range(n):
    for j in range(i):
        if li[i] > li[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += li[i]
print(max(dp))