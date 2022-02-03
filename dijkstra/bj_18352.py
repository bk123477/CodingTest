import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

# n=도시개수, m=도로개수, k=거리정보, x=start
n, m, k, x = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append((b, 1))

def dijkstra(x): # 다익스트라 알고리즘 수행
    q = []
    heapq.heappush(q, (0, x))
    distance[x] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(x)

if k not in distance:
    print(-1)
else:
    for i in range(1, n+1):
        if distance[i] == k:
            print(i)

n, m, k, x = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
visited = [False] * (n+1)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    distance[start] = 0
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                distance[i] = distance[now] + 1
                queue.append(i)

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)

bfs(graph, x, visited)

if k not in distance:
    print(-1)
else:
    for i in range(1, n+1):
        if k == distance[i]:
            print(i)