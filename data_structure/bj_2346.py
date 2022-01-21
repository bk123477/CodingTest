import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
li = list(map(int, sys.stdin.readline().rstrip().split()))
my_deque = deque()
array = deque()
for i in range(n):
    my_deque.append(li[i])
    array.append(i+1)

cnt = 0
result = []
while True:
    tomove = my_deque.popleft()
    index = array.popleft()
    cnt += 1
    result.append(index)
    if cnt == n:
        break
    if tomove > 0:
        for _ in range(tomove - 1):
            temp = my_deque.popleft()
            t_i = array.popleft()
            my_deque.append(temp)
            array.append(t_i)
    else:
        for _ in range(abs(tomove)):
            temp = my_deque.pop()
            t_i = array.pop()
            my_deque.appendleft(temp)
            array.appendleft(t_i)
for v in result:
    print(v, end=" ")