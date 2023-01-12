

import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input().rstrip())
numList = list(map(int, input().rstrip().split()))

left = 0
right = len(numList) - 1
result = -1

while left <= right:
    mid = (left + right) // 2
    if numList[mid] == mid:
        result = mid
        break
    elif numList[mid] > mid:
        right = mid - 1
    else:
        left = mid + 1

print(result)