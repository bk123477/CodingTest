import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().rstrip().split())
k = int(input().rstrip()) # start node
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for i in graph[node]:
            cost = distance[node] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(k)
for i in range(1, v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])