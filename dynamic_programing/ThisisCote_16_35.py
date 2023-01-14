# 못 풂. 접근 방식 보기.

import sys
input = sys.stdin.readline

n = int(input().rstrip())

# 못생긴 수는 2,3,5 만을 소인수로 가지는 수
dp = [0] * n
dp[0] = 1

# 2, 3, 5배를 위한 인덱스
i2 = i3 = i5 = 0
# 처음 곱셈값 초기화
next2, next3, next5 = 2, 3, 5

for l in range(1, n):
    dp[l] = min(next2, next3, next5)
    if dp[l] == next2:
        i2 += 1
        next2 = dp[i2] * 2
    if dp[l] == next3:
        i3 += 1
        next3 = dp[i3] * 3
    if dp[l] == next5:
        i5 += 1
        next5 = dp[i5] * 5

print(dp[n-1])