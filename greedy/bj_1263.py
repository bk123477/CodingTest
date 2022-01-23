import sys

n = int(sys.stdin.readline().rstrip())
order = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    order.append((b, a)) # 끝내야 하는 시간, 걸리는 시간
order.sort()

time = 0
while True:
    temp_time = time
    flag = True
    for b, a in order:
        temp_time += a
        if b < temp_time:
            flag = False
            break
    if flag == False:
        time -= 1
        print(time)
        break
    else:
        time += 1