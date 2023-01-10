

import sys
input = sys.stdin.readline

n = int(input().rstrip())
numArray = []
for _ in range(n):
    numArray.append(int(input().rstrip()))

numArray.sort(reverse=True)

for data in numArray:
    print(data, end=' ')