import sys
from collections import deque
n, l = map(int, sys.stdin.readline().rstrip().split())
deq = deque()
flag = 0
while True:
    if l > 100:
        flag = 1
        break
    if l % 2 != 0: # l이 홀수
        if n%l == 0: # 나누어 떨어짐 가운데 수가 정수
            mid = n//l
            min_num = mid - (l//2)
            max_num = mid + (l//2)
            if min_num < 0:
                flag = 1
                break
            else:
                for v in range(min_num, max_num + 1):
                    deq.append(v)
                break
    else: # l이 짝수
        if n/l - n//l == 0.5:
            mid = n//l
            min_num = mid - (l//2) + 1
            max_num = mid + (l//2)
            if min_num < 0 :
                flag = 1
                break
            else:
                for v in range(min_num, max_num + 1):
                    deq.append(v)
                break
    l += 1

# flag == 1 -> print(-1)
if flag == 1:
    print(-1)
else:
    for i in range(l):
        print(deq.popleft(), end = " ")