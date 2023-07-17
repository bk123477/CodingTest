# acmicpc.net/problem/10282

import sys
import heapq
INF = 1e9
input = sys.stdin.readline

def dijkstra():
    n, d, c = map(int, input().split()) # n = 컴퓨터 개수, d = 의존성 개수, c = 해킹당한 컴퓨터
    computers = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)

    for _ in range(d):
        a, b, s = map(int, input().split())
        computers[b].append((a, s))
    
    q = []
    heapq.heappush(q, (0, c))
    distance[c] = 0
    li = []
    li.append(c)
    final_node = []
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for i in computers[node]:
            cost = dist = i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                li.append(i[0])
                heapq.heappush(q, (cost, i[0]))
    li = set(li)
    for v in li:
        final_node.append(distance[v])
    print(len(li), max(final_node))

t = int(input())
for _ in range(t):
    dijkstra()
