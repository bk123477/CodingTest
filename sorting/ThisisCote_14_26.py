# acmicpc.net/problem/1715

import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
q = []
for _ in range(n):
    heapq.heappush(q, int(input().rstrip()))

result = 0
while len(q) >= 2:
    first = heapq.heappop(q)
    second = heapq.heappop(q)
    result += first + second
    heapq.heappush(q, first+second)

print(result)