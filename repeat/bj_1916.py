# acmicpc.net/problem/1916

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = 1e9

N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수

city = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

# (출발 도시 번호, 도착 도시 번호, 버스의 비용)
for _ in range(M):
    start, end, cost = map(int, input().split())
    city[start].append((end, cost)) # list[idx]에 (end, cost) 튜플로 추가

start_city, end_city = map(int, input().split())

def dijkstra(start):
    q = []
    heappush(q, (0, start)) # heapq에 (cost, current) 튜플로 추가
    distance[start] = 0
    while q:
        cost, current = heappop(q)
        if distance[current] < cost: # 이미 최소비용 구해진 경우
            continue
        for i in city[current]: # 현재 도시에서 버스로 갈 수 있는 도시들 탐색
            c = cost + i[1] 
            if c < distance[i[0]]: # 최소 비용이 새로 구해진 경우
                distance[i[0]] = c
                heappush(q, (c, i[0]))

dijkstra(start_city)
print(distance[end_city])