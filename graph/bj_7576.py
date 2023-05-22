# acmicpc.net/problem/7576

from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * m for _ in range(n)]

box = []
for _ in range(n):
    box.append(list(map(int, input().split())))

queue = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == False and box[nx][ny] == 0:
                visited[nx][ny] = True
                box[nx][ny] = box[x][y] + 1
                queue.append([nx, ny])

bfs()
result = 0
flag = False
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            flag = True
            break
        result = max(result, box[i][j])
    if flag:
        break
if flag:
    print(-1)
else:
    print(result - 1)