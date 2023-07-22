# acmicpc.net/problem/11404

import sys
import heapq
input = sys.stdin.readline
INF = 1e9

def Floyid(start):
    visit = [False] * (N+1)
    cost = [INF] * (N+1)
    q = []
    q.append((0, start))
    visit[start] = True
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
    for i in range(1, N+1):
        if cost[i] == INF:
            print(0, end=" ")
        else:
            print(cost[i], end=" ")
    print()

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

for i in range(1, N+1):
    Floyid(i)