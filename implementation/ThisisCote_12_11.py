# acmicpc.net/problem/3190

import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
k = int(input().rstrip())
gameMap = [[0 for _ in range(n+1)] for _ in range(n+1)] # 2차원 list comprehension

for _ in range(k):
    x, y = map(int, input().rstrip().split())
    gameMap[y][x] = 1

count = 0
nowX = nowY = 1
l = int(input().rstrip())
dirInfo = []
for _ in range(l):
    cnt, direction = input().rstrip().split()
    dirInfo.append((int(cnt), direction))

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0] # 북, 동, 남, 서
dir = 1
index = 0
snakeMap = deque()
snakeMap.append((1,1))
while True:
    nX = nowX+dx[dir]
    nY = nowY+dy[dir]
    count += 1
    if nX == 0 or nX>n or nY == 0 or nY>n: # 벽에 부딪혔을 때
        break

    flag = 0
    for body in snakeMap:
        if nX == body[0] and nY == body[1]: # 몸에 부딪혔을 때
            flag = 1
            break

    if flag == 1:
        break
    else:
        if gameMap[nX][nY] == 1: # 사과 있을 경우
            snakeMap.append((nX, nY))
            gameMap[nX][nY] = 0
        else: # 사과 없을 경우
            snakeMap.append((nX, nY))
            snakeMap.popleft()
    
    nowX = nX
    nowY = nY

    if index<l and count == dirInfo[index][0]:
        if dirInfo[index][1] == 'L':
            dir = (dir - 1) % 4
        else:
            dir = (dir + 1) % 4
        index += 1

print(count)