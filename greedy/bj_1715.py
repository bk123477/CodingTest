import sys
import heapq

n = int(sys.stdin.readline().rstrip())
q = []
for _ in range(n):
    heapq.heappush(q, int(sys.stdin.readline().rstrip()))
result = 0
for _ in range(n-1):
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    result += a+b
    heapq.heappush(q, a+b)
print(result)