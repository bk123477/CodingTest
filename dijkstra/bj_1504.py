import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start)) # (거리, 노드)
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

n, e = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
first_distance = [INF] * (n+1)
v1_v2_distance = [INF] * (n+1)
v1_distance = [INF] * (n+1)
v2_distance = [INF] * (n+1)

for _ in range(e):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().rstrip().split())

dijkstra(1, first_distance) # 1부터 v1 or 1부터 v2까지 거리
dijkstra(v1, v1_v2_distance) # v1~v2거리
dijkstra(v1, v1_distance) # v1부터 n까지의 거리
dijkstra(v2, v2_distance) # v2부터 n까지의 거리

first_result = first_distance[v1] + v1_v2_distance[v2] + v2_distance[n]
second_result = first_distance[v2] + v1_v2_distance[v2] + v1_distance[n]

if first_result >= INF and second_result >= INF:
    print(-1)
else:
    print(min(first_result, second_result))
