from collections import defaultdict
import sys
input = sys.stdin.readline


def dfs(n):
    if data[n] != 0:
        return data[n]

    data[n] = dfs(n // p) + dfs(n // q)
    return data[n]

n, p, q = map(int, input().split())
# defaultdict를 사용하여 dict 자료형에 데이터 매핑.
# defaultdict를 사용하면 초기화 하는 과정을 간단히 할 수 있다.
data = defaultdict(int) 
data[0] = 1

print(dfs(n))