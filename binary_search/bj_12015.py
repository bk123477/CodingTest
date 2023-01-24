# acmicpc.net/problem/12015
# DP를 활용하지 못하는 문제. bisect를 사용해야 함.
# 이전 것 보다 크면, 바로 LIS에 append
# 이전 것 보다 작으면, LIS에서 현재 item보다 작은 값의 인덱스를 리턴해서 그 자리에 item을 넣어 줌.

import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = [*map(int, input().split())]

LIS = [A[0]]

for item in A:
    if LIS[-1] < item:
        LIS.append(item)
    else:
        idx = bisect_left(LIS, item)
        LIS[idx] = item

print(len(LIS))