import sys
from collections import deque

n, l = map(int, sys.stdin.readline().rstrip().split()) # n:물이 새는 곳 개수, l:테이프길이
li = list(map(int, sys.stdin.readline().rstrip().split()))
li.sort()
cnt = 1
start = li[0] - 0.5
end = li[0]- 0.5 + l
for loc in li:
    if start <= loc - 0.5 and loc + 0.5 <= end:
        continue
    else:
        start = loc - 0.5
        end = loc - 0.5 + l
        cnt += 1
print(cnt)