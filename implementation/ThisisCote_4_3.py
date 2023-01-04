# 이 문제 틀림..
# 나중에 다시 풀어보기!

import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
nowX, nowY, dir = map(int, input().rstrip().split())

gameMap = []
for _ in range(n):
    tempList = list(map(int, input().rstrip().split()))
    gameMap.append(tempList)

# 현재 바라보고 있는 위치 : 0:북쪽, 1:동쪽, 2:남쪽, 3:서쪽
# next direction = 반 시계 방향
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0] # 북, 서, 남, 동
result = 1
gameMap[nowX][nowY] = -1
allDirection = 0

while True:
    nextDx = nowX+dx[(dir+1)%4]
    nextDy = nowY+dy[(dir+1)%4]

    if allDirection == 4:
        nextDx = nowX+dx[(dir+2)%4]
        nextDy = nowY+dy[(dir+2)%4]
        if gameMap[nextDx][nextDy] == 1:
            break
        
        allDirection = 0
        nowX = nextDx
        nowY = nextDy
        continue

    if gameMap[nextDx][nextDy] == -1 or gameMap[nextDx][nextDy] == 1: # 가본 칸 or 바다일 경우
        allDirection += 1
        continue
    
    gameMap[nextDx][nextDy] = -1
    nowX = nextDx
    nowY = nextDy
    result+=1
    allDirection = 0

print(result)