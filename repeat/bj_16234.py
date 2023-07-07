# acmicpc.net/problem/16234

import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())

nations = []
count = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    nations.append(list(map(int, input().split())))

def bfs(x, y):
    q = deque()
    global visit
    union = []
    total = 0
    q.append((x, y))
    union.append((x, y))
    total += nations[x][y]
    visit[x][y] = True
    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nx, ny = cur_x +dx[i], cur_y + dy[i]
            if 0<=nx<N and 0<=ny<N and not visit[nx][ny]:
                if L <= abs(nations[cur_x][cur_y] - nations[nx][ny]) <= R:
                    q.append((nx, ny))
                    union.append((nx, ny))
                    total += nations[nx][ny]
                    visit[nx][ny] = True
    if len(union) == 1:
        return False
    else:
        each = total // len(union)
        for nation in union:
            nations[nation[0]][nation[1]] = each
        return True

while True:
    visit = [[False] * N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                second_flag = bfs(i, j)
                if second_flag:
                    flag = True
    if flag:
        count += 1
    else:
        print(count)
        break