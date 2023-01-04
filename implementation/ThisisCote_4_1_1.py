import sys
input = sys.stdin.readline

n = int(input().rstrip())
moves = list(input().rstrip().split())

nowX = nowY = 1
for move in moves:
    if move == 'L':
        if nowY == 1: continue
        else: nowY -= 1
    elif move == 'R':
        if nowY == n: continue
        else: nowY += 1
    elif move == 'U':
        if nowX == 1: continue
        else: nowX -= 1
    else:
        if nowX == n: continue
        else: nowX += 1

print(nowX, nowY)

# sol) 이렇게 풀어도 되지만
# dx = [0, 0, -1, 1]
# dy = [-1, -1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']
# 로 관리하면서 for문 돌리면 더 간단하게 코딩 가능.