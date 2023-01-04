import sys
input = sys.stdin.readline

# 나이트의 이동은 수평 두칸 이동, 수직 한칸 or 수직 두칸 이동, 수평 한칸
# 8x8 평면상에서 현재 나이트 좌표 입력 받음 a1~h8

pos = input().rstrip()
nowX = pos[0]
nowY = int(pos[1])

result = 0
dx = [1, -1, 1, -1, -2, -2, 2, 2]
dy = [2, 2, -2, -2, 1, -1, 1, -1]

for i in range(8):
    if (nowX == 'a' and dx[i] < 0) or (nowX == 'b' and dx[i] < -1): continue
    if (nowX == 'g' and dx[i] > 1) or (nowX == 'h' and dx[i] > 0): continue
    if (nowY == 1 and dy[i] < 0) or (nowY == 2 and dy[i] < -1): continue
    if (nowY == 7 and dy[i] > 1) or (nowY == 8 and dy[i] > 0): continue
    result += 1

print(result)