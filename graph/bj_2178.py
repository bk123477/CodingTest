import sys
from collections import deque
input = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1] # 상, 하, 좌, 우

n, m = map(int, input().rstrip().split())
graph = []
for _ in range(n): # 각각의 수들은 붙어서 입력됨.
    graph.append(list(input().rstrip()))

def bfs():
    queue = deque([(0, 0)])
    while queue:
        now_node= queue.popleft()
        now_y = now_node[0] # 현재 y좌표
        now_x = now_node[1] # 현재 x좌표
        for i in range(4):
            next_y = now_y + dy[i] # 다음 y좌표
            next_x = now_x + dx[i] # 다음 x좌표
            # 다음 좌표의 그래프 범위 탐색 및 벽인지 판단
            if 0 <= next_y < n and 0 <= next_x < m and graph[next_y][next_x] == '1':
                graph[next_y][next_x] = str(int(graph[now_y][now_x])+1) # int로 바꿔 더한 후 다시 문자로 넣어줌
                queue.append((next_y, next_x))
bfs()
print(int(graph[n-1][m-1]))