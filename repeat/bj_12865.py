# acmicpc.net/problem/12865

import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # N = 물품 수, K = 버틸 수 있는 무게

nList = [[0,0]]
dp = [[0]*(K+1) for _ in range(N+1)]

for _ in range(N):
    nList.append(list(map(int, input().split())))

for i in range(1, N+1): # i = 물건 개수 도는 index
    for j in range(1, K+1): # j = 배낭 무게 도는 index
        w = nList[i][0]
        v = nList[i][1]

        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[N][K])