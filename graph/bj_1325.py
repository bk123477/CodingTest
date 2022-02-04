import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    visited = [False] * (n+1)
    visited[start] = True
    count = 0
    while queue:
        now = queue.popleft()
        for node in graph[now]:
            if not visited[node]:
                visited[node] = True
                count += 1
                queue.append(node)
    return count

n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
counting = [0] * (n+1)
max_count = 0
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[b].append(a)

for i in range(1, n+1):
    counting[i] = bfs(i)
    if counting[i] > max_count:
        max_count = counting[i]

for i in range(1, n+1):
    if counting[i] == max_count: print(i, end=' ')