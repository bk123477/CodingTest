# 이 문제 못 풀었음. 나중에 다시 풀기

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
miro = []
visited = [[False for _ in range(m)] for _ in range(n)] 
for _ in range(n):
    miro.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] # 상, 하, 좌, 우

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if miro[nx][ny] == 0:
                continue
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx, ny))
    return miro[n-1][m-1]

print(bfs(0, 0))