# acmicpc.net/problem/1744

import sys
input = sys.stdin.readline

N = int(input())
negative, positive, one = [], [], []
for _ in range(N):
    temp = int(input())
    if temp <= 0:
        negative.append(temp)
    elif temp == 1:
        one.append(temp)
    else:
        positive.append(temp)

negative.sort()
positive.sort(reverse=True)

result = 0
if len(positive) % 2 == 0:
    for i in range(len(positive) // 2):
        result += positive[2*i] * positive[2*i+1]
else:
    for i in range(len(positive) // 2):
        result += positive[2*i] * positive[2*i+1]
    result += positive[len(positive)-1]

if len(negative) % 2 == 0:
    for i in range(len(negative) // 2):
        result += negative[2*i] * negative[2*i+1]
else:
    for i in range(len(negative) // 2):
        result += negative[2*i] * negative[2*i+1]
    result += negative[len(negative)-1]

for _ in range(len(one)):
    result += 1
print(result)