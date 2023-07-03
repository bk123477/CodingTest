# acmicpc.net/problem/7576

from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visit = [[False] * M for _ in range(N)]
house = []
for _ in range(N):
    house.append(list(map(int, input().split())))

queue = deque()
for i in range(N):
    for j in range(M):
        if house[i][j] == 1:
            queue.append((i, j))


def bfs():
    while queue:
        current = queue.popleft()
        visit[current[0]][current[1]] = True
        for i in range(4):
            nx, ny = current[0]+dx[i], current[1]+dy[i]
            if 0<=nx<N and 0<=ny<M and visit[nx][ny] == False and house[nx][ny] == 0:
                house[nx][ny] = house[current[0]][current[1]] + 1
                visit[nx][ny] = True
                queue.append((nx, ny))

bfs()
flag = False
cnt = 0
for i in range(N):
    for j in range(M):
        if house[i][j] == 0:
            flag = True
            break
    if flag:
        break
    tmpmax = max(house[i])
    cnt = max(cnt, tmpmax)

if flag:
    print(-1)
else:
    print(cnt-1)