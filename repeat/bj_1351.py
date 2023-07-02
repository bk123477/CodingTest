# acmicpc.net/problem/1351

import sys
from collections import defaultdict
input = sys.stdin.readline

def dfs(num):
    if data[num] != 0:
        return data[num]
    
    data[num] = dfs(num // P) + dfs(num // Q)
    return data[num]

N, P, Q = map(int, input().split())
data = defaultdict(int)
data[0] = 1
print(dfs(N))