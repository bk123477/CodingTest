

import sys
input = sys.stdin.readline
INF = 10001

n, m = map(int, input().rstrip().split())
coins = []
for _ in range(n):
    coins.append(int(input().rstrip()))

coins.sort()

dp = [INF for _ in range(10001)]
for coin in coins:
    dp[coin] = 1 # 가장 작은 화폐 단위의 값은 이거 하나로만 만들 수 있음.

for i in range(coins[0]+1, m+1):
    for coin in coins:
        dp[i] = min(dp[i], dp[i-coin]+1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])