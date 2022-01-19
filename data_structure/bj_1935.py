import sys
from collections import deque

n = int(sys.stdin.readline().rstrip()) # 숫자 개수
operation = list(sys.stdin.readline().rstrip())
number = {}
for i in range(n):
    number[chr(65+i)] = int(sys.stdin.readline().rstrip())
my_stack = deque()

for i in operation:
    if 'A' <= i <= 'Z': # dictionary에서 해당key에서 value 뽑아오기
        my_stack.append(number[i])
    else:
        two = my_stack.pop()
        one = my_stack.pop()
        if i == '+':
            my_stack.append(one + two)
        elif i == '-':
            my_stack.append(one - two)
        elif i == '*':
            my_stack.append(one * two)
        else:
            my_stack.append(one / two)
print("%.2F" %(my_stack.pop()))