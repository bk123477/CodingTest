import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m): # 간선 정보 입력, 무방향 그래프
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0 # 연결 요소의 개수 담는 변수
for i in range(1, n+1):
    if visited[i]: # 이미 방문 처리 된 노드는 건너 뜀
        continue
    queue = deque([i])
    visited[i] = True
    while queue:
        node = queue.popleft()
        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
    count += 1 # 연결 요소 카운팅

print(count)