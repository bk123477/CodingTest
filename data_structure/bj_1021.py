from collections import deque
import sys
n, m = map(int, input().split())
example = list(map(int, input().split()))

data = deque()
cnt = 0
for i in range(1, n + 1):
    data.append(i)
for i in example:
    while True:
        if data[0] == i:
            data.popleft()
            break
        else:
            if data.index(i) <= len(data)//2:
                data.rotate(-1)
                cnt += 1
            else:
                data.rotate(1)
                cnt += 1

print(cnt)