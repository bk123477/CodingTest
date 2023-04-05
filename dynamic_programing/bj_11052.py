# acmicpc.net/problem/11052

import sys
input = sys.stdin.readline

n = int(input())
pscard = list(map(int, input().split()))

dp = [0] * (n+1)
dp[1] = pscard[0]

for i in range(2, n+1):
    tempList = []
    for j in range(len(pscard)):
        if j+1 > i: break
        else:
            tempList.append(pscard[j] + dp[i-(j+1)])
    dp[i] = max(tempList)

print(dp[n])