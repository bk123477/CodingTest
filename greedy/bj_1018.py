import sys

row, col = map(int, sys.stdin.readline().rstrip().split())
input_board = []
for _ in range(row):
    input_board.append(list(sys.stdin.readline().rstrip()))

# check할 보드판 만들기
start_b = [j for _ in range(4) for j in ('B', 'W')]
start_w = [j for _ in range(4) for j in ('W', 'B')]
check_b = []
check_w = []
for i in range(8):
    if i % 2 == 0:
        check_b.append(start_b)
        check_w.append(start_w)
    else:
        check_b.append(start_w)
        check_w.append(start_b)
min_w = 64
min_b = 64
for i in range(row-7):
    for j in range(col-7): # 8*8 보드판 시작 부분 인덱스
        cnt_b = 0
        cnt_w = 0
        for r in range(8):
            for c in range(8):
                if input_board[i+r][j+c] != check_b[r][c]:
                    cnt_b += 1
                if input_board[i+r][j+c] != check_w[r][c]:
                    cnt_w += 1
        if cnt_b < min_b:
            min_b = cnt_b
        if cnt_w < min_w:
            min_w = cnt_w
print(min(min_w, min_b))