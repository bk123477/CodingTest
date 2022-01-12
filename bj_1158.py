import sys
from collections import deque
'''
# other solution<!best!>
n, k = map(int, sys.stdin.readline().rstrip().split())

stk = [i for i in range(1, n+1)]
res_list = []

num = 0 # index

for _  in range(n):
    num += k-1
    if(num >= len(stk)):
        num = num%len(stk)
    res_list.append(stk.pop(num))

print('<' + ", ".join(map(str, res_list)) + '>')
'''
# my solution
n, k = map(int, sys.stdin.readline().rstrip().split())
queue = deque()
result = [0] * n
cnt = 0
#deque init
for i in range(1,n+1):
    queue.append(i)
while cnt < n:
    tempcnt = 0
    while tempcnt < k:
        a = queue.popleft()
        if(tempcnt == k-1):
            result[cnt] = a
            cnt += 1
            break
        else:
            queue.append(a)
            tempcnt += 1
print('<' + ", ".join(map(str, result))+'>')
