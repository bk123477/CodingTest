# acmicpc.net/problem/18428
# 못 풂. 나중에 다시 풀기

import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input().rstrip())
board = []
teachers = []
spaces = []

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))
        if board[i][j] == 'X':
            spaces.append((i, j))

def watch(x, y, direction):
    # 왼쪽 방향
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S': # 학생인 경우
                return True
            if board[x][y] == 'O': # 장애물일 경우
                return False
            y -= 1
    if direction == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1
    if direction == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1
    return False

# 장애물 설치 이후, 학생 감지 검사
def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False

for data in combinations(spaces, 3):
    for x, y in data:
        board[x][y] = 'O'
    if not process():
        find = True
        break
    for x, y in data:
        board[x][y] = 'X'

if find:
    print("YES")
else:
    print("NO")
            