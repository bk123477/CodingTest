# acmicpc.net/problem/18353
# 못 풂.

import sys
input = sys.stdin.readline

n = int(input().rstrip())
soldiers = list(map(int, input().rstrip().split()))
soldiers.reverse()

dp = [1] * n

# 가장 긴 증가하는 부분 수열 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if soldiers[j] < soldiers[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(n - max(dp))