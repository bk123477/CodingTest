import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
path = [INF] * (n+1) # 간선 연결 기록할 리스트
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c)) # 양방향으로 연결해 줌

q = []
heapq.heappush(q, (0, 1))
distance[1] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist: continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))
            path[i[0]] = [now, i[0]] # i[0]와 연결된 가장 최근의 노드 기록
print(n-1)
for i in range(n+1):
    if path[i] != INF:
        print(path[i][0], path[i][1])