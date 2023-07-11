# acmicpc.net/problem/1753

import sys
import heapq
input = sys.stdin.readline
INF = 1e9

V, E = map(int, input().split())
K = int(input()) # 시작 정점 번호

graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

distance = [INF] * (V+1)

q = [(0, K)]
distance[K] = 0
while q:
    dist, node = heapq.heappop(q)
    if distance[node] < dist:
        continue
    for next in graph[node]:
        cost = dist + next[1]
        if cost < distance[next[0]]:
            distance[next[0]] = cost
            heapq.heappush(q, (cost, next[0]))

print(distance)