# acmicpc.net/problem/2225

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
result = [[0]*(N+1) for _ in range(K+1)]

result[1] = [1] * (N+1)

for i in range(1, K+1):
    result[i][0] = 1
    for j in range(1, N+1):
        result[i][j] = (result[i-1][j] + result[i][j-1]) % 1000000000

print(result[K][N])