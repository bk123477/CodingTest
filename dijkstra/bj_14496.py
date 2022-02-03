import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

a, b = map(int, input().rstrip().split())
n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    start, end = map(int, input().rstrip().split())
    graph[start].append((end, 1))
    graph[end].append((start, 1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 거리, 노드
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(a)
if distance[b] == INF:
    print(-1)
else:
    print(distance[b])