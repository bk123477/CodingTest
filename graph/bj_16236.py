# acmicpc.net/problem/16236
# 못 풂..

import sys
from collections import deque
input = sys.stdin.readline

bx, by = 0,0
baby = 2
eatCnt = 0
fishCnt = 0
fishPos = []
time = 0
dx = (0,0,1,-1)
dy = (1,-1,0,0)
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if 0 < graph[i][j] <= 6:
            fishCnt +=1
            fishPos.append((i,j))
        elif graph[i][j] == 9:
            bx, by = i,j
graph[bx][by]=0

def bfs(bx,by):
    q = deque([(bx, by, 0)])
    distList = []
    visited = [[False] * n for _ in range(n)]
    visited[bx][by] = True
    minDist = int(1e9)
    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] <= baby: # 이동할 수 있는 칸
                    visited[nx][ny] = True
                    if 0 < graph[nx][ny] < baby: # 먹을 수 있는 경우
                        minDist = dist
                        distList.append((dist + 1, nx, ny))
                    if dist + 1 <= minDist: # 아직 최소 거리가 아닐 경우
                        q.append((nx, ny, dist + 1))
    if distList:
        distList.sort()
        return distList[0]
    else:
        return False

while fishCnt :
    result = bfs(bx, by)
    if not result:
        break
    bx,by = result[1],result[2]
    time += result[0]
    eatCnt += 1
    fishCnt -= 1
    if baby == eatCnt:
        baby += 1
        eatCnt = 0
    graph[bx][by] = 0

print(time)