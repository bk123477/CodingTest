import sys

n, kim, lim = map(int, sys.stdin.readline().rstrip().split())
max_n = max(kim, lim)
min_n = min(kim, lim)
cnt = 1
while True:
    if 2**cnt >= max_n:
        break
    else:
        cnt += 1

# cnt = 최대로 나올 수 있는 답. 이제 범위 줄여야함
while True:
    check = cnt - 1
    for i in range(2): 
        if (2**check)*i + 1 <= min_n < max_n <= (2**check)*(i+1):
            cnt -= 1
            break
    if check == cnt:
        continue
    else:
        cnt += 1
        break
print(cnt)