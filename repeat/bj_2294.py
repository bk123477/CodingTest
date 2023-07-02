# acmicpc.net/problem/2294

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
result = [-1] * (K+1)
for _ in range(N):
    coin = int(input())
    coins.append(coin)
coins.sort()

for coin in coins:
    if coin <= K:# 동전 한개로 만들 수 있는 경우 전처리
        result[coin] = 1

for i in range(1, K+1):
    if result[i] != -1: # 동전 한개로 만들 수 있는 경우(전처리 됨)
        continue
    candidate = []
    for coin in coins:
        if i-coin < 0: # index error
            break
        if result[i-coin] != -1: # 이 동전으로 못 만드는 경우
            candidate.append(result[i-coin])
    if len(candidate) > 0:
        result[i] = min(candidate)+1

print(result[K])