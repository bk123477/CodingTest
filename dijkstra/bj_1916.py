import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input().rstrip()) # 도시 개수
m = int(input().rstrip()) # 버스 개수
graph = [[] for _ in range(n+1)]
cost = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))

start, end = map(int, input().rstrip().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # (거리, 노드)
    cost[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if cost[node] < dist:
            continue
        for i in graph[node]:
            c = cost[node] + i[1]
            if c < cost[i[0]]:
                cost[i[0]] = c
                heapq.heappush(q, (c, i[0]))
dijkstra(start)
print(cost[end])