# acmicpc.net/problem/15686
# sol) 아예 못 풀었음. 추후 다시 풀기.
# python의 combinations 라이브러리 사용하는 문제.
import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().rstrip().split()))
    for c in range(n):
        if data[c] == 1: house.append((r, c))
        elif data[c] == 2: chicken.append((r, c))

candidates = list(combinations(chicken, m)) # chicken중 m개를 뽑는 것. list로 형변환

def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx) + abs(hy-cy))
        result += temp
    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)