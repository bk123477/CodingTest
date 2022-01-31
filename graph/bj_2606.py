import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, start, visited):
    count = 0
    queue = deque([start])
    visited[start] = True
    while queue:
        cur = queue.popleft()
        for i in graph[cur]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count += 1
    return count

n = int(input().rstrip()) # 컴퓨터 개수
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

link_num = int(input().rstrip()) # 연결 정보 개수
for _ in range(link_num):
    index, information = map(int, input().rstrip().split())
    graph[index].append(information)
    graph[information].append(index)

result = bfs(graph, 1, visited)
print(result)