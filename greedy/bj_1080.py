import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
change_maps = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)] # 바뀌는 맵
result_maps = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)] # 목표 맵
cnt = 0

def change3x3(x, y, arr): # 통째로 3x3 행렬 뒤집음
    for i in range(x, x+3):
        for j in range(y, y+3):
            change_maps[i][j] = 1 - change_maps[i][j]

for i in range(0, n-2):
    for j in range(0, m-2):
        if change_maps[i][j] != result_maps[i][j]:
            change3x3(i, j, change_maps)
            cnt += 1
result = True
for i in range(n):
    for j in range(m):
        if change_maps[i][j] != result_maps[i][j]:
            result = False
if result:
    print(cnt)
else:
    print(-1)