# acmicpc.net/problem/16234

import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().rstrip().split())
worldMap = []
count = 0
for _ in range(N):
    worldMap.append(list(map(int, input().rstrip().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    union = []
    totalPeople = 0
    q.append((x, y))
    union.append((x, y))
    totalPeople += worldMap[x][y]
    global visited
    visited[x][y] = 1
    while q:
        curX, curY = q.popleft()
        for i in range(4):
            nx = curX + dx[i]
            ny = curY + dy[i]
            if 0 <= nx and nx < N and 0 <= ny and ny < N and visited[nx][ny] == 0:
                if L <= abs(worldMap[curX][curY] - worldMap[nx][ny]) and abs(worldMap[curX][curY] - worldMap[nx][ny]) <= R:
                    q.append((nx, ny))
                    union.append((nx, ny))
                    totalPeople += worldMap[nx][ny] 
                    visited[nx][ny] = 1
    if len(union) == 1:
        return False
    else:
        eachPeople = totalPeople // len(union)
        for nation in union:
            worldMap[nation[0]][nation[1]] = eachPeople
        return True


while True:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                secondFlag = bfs(i, j)
                if secondFlag: flag = True
    if flag:
        count += 1
        continue
    else:
        print(count)
        break