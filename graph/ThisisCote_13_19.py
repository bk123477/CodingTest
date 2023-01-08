# acmicpc.net/problem/14888
# 못 풂. 다시 풀어보기....

import sys
from collections import deque
from itertools import permutations
INF = 1e9
input = sys.stdin.readline

N = int(input().rstrip())
data = list(map(int, input().rstrip().split()))
add, sub, mul, div = map(int, input().rstrip().split())

minValue = INF
maxValue = -INF

def dfs(i, now):
    global minValue, maxValue, add, sub, mul, div
    # 모든 연산자 다 사용한 경우, 최소값, 최대값 업데이트
    if i == N:
        minValue = min(minValue, now)
        maxValue = max(maxValue, now)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now/data[i]))
            div += 1

dfs(1, data[0])
print(maxValue)
print(minValue)