import sys
from collections import deque
input = sys.stdin.readline

result_dfs = []
result_bfs = []

def dfs(graph, start, visited):
    visited[start] = True
    result_dfs.append(start)
    for k in graph[start]:
        if not visited[k]:
            dfs(graph, k, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    result_bfs.append(start)
    while queue:
        temp = queue.popleft()
        for i in graph[temp]:
            if not visited[i]:
                queue.append(i)
                result_bfs.append(i)
                visited[i] = True

n, m, v = map(int, input().rstrip().split()) #정점 개수, 간선 개수, 시작 정점
graph = [[] for _ in range(n+1)] # 정점은 graph[1] ~ graph[n]
for _ in range(m): # 간선 정보 입력 받음
    front, rear = map(int, input().rstrip().split())
    graph[front].append(rear)
    graph[rear].append(front)
    graph[front].sort()
    graph[rear].sort()

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)
dfs(graph, v, visited_dfs)
bfs(graph, v, visited_bfs)
for v in result_dfs:
    print(v, end=' ')
print('\n', end='')
for v in result_bfs:
    print(v, end=' ')