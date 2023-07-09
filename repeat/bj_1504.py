# acmicpc.net/problem/1504

import sys
import heapq
INF = 1e9
input = sys.stdin.readline

def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist: # 이미 최단거리 구한 상태
            continue
        for i in graph[node]:
            cost = distance[node] + i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v_one, v_two = map(int, input().split())

first_distance = [INF] * (N+1) # 1에서 나머지 노드까지 거리
v1_distance = [INF] * (N+1)  # v1에서 나머지 노드까지 거리
v2_distance = [INF] * (N+1) # v2에서 나머지 노드까지 거리
v1_v2_distance = [INF] * (N+1) # v1, v2 사이의 거리

dijkstra(1, first_distance)
dijkstra(v_one, v1_v2_distance)
dijkstra(v_one, v1_distance)
dijkstra(v_two, v2_distance)

first_result = first_distance[v_one] + v1_v2_distance[v_two] + v2_distance[N]
second_result = first_distance[v_two] + v1_v2_distance[v_two] + v1_distance[N]
if first_result >= INF and second_result >= INF:
    print(-1)
else:
    print(min(first_result, second_result))