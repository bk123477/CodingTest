import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
queue = deque()
for i in range(1, n+1):
    queue.append(i)

cnt = 0
track = 0
while cnt < (n-1):
    if track == 0:
        queue.popleft()
        track = 1
        cnt += 1 # queue에서 제거 했을 때만 cnt += 1
    else:
        temp = queue.popleft()
        queue.append(temp)
        track = 0
print(queue.pop())