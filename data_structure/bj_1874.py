import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
my_stack = deque()
number = 1
flag = 0
result = []
for i in range(n):
    target = int(sys.stdin.readline().rstrip())
    while number <= target:
        my_stack.append(number)
        result.append('+')
        number += 1
    if my_stack.pop() == target:
        result.append('-')
    else:
        flag = -1
if flag == -1:
    print('No')
else:
    for i in result:
        print(i)