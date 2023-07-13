# acmicpc.net/problem/3190

import sys
from collections import deque
input = sys.stdin.readline

N = int(input()) # N x N 보드
K = int(input()) # K = 사과의 개수

board = [[0] * (N+1) for _ in range(N+1)]
for _ in range(K):
    x, y = map(int, input().split())
    board[x][y] = 1 # 사과는 1

L = int(input()) # L = 방향 변환 횟수
change_info = deque()
for _ in range(L):
    x, c = input().split()
    change_info.append((int(x), c))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1] # 북, 동, 남, 서

direction = 1 # 0 = 북, 1 = 동, 2 = 남, 3 = 서

cnt = 0
head_x, head_y = 1, 1
board[head_x][head_y] = -1 # 몸 = -1
body = deque()
body.append((1, 1))
while True:
    cnt += 1
    cur_x, cur_y = head_x + dx[direction], head_y + dy[direction]
    if cur_x <= 0 or cur_x > N or cur_y <= 0 or cur_y > N: # 벽에 부딪힌 경우
        break
    elif board[cur_x][cur_y] == -1: # 몸에 부딪힌 경우
        break

    if board[cur_x][cur_y] == 1: # 사과 먹은 경우
        head_x, head_y = cur_x, cur_y # 몸 길이 증가, 꼬리는 그대로
        board[head_x][head_y] = -1 # 몸으로 바꿔줌
        body.append((head_x, head_y))
    elif board[cur_x][cur_y] == 0: # 빈 칸인 경우
        head_x, head_y = cur_x, cur_y
        board[head_x][head_y] = -1 # 몸으로 바꿔줌
        body.append((head_x, head_y))
        tail_x, tail_y = body.popleft()
        board[tail_x][tail_y] = 0

    if len(change_info) == 0:
        continue
    else:
        if cnt == change_info[0][0]:
            x, c = change_info.popleft()
            if c == 'L':
                direction -= 1
                if direction == -1:
                    direction = 3
            else:
                direction += 1
                if direction == 4:
                    direction = 0

print(cnt)