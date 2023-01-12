

import sys
input = sys.stdin.readline

n = int(input().rstrip())
warehouse = list(map(int, input().rstrip().split()))

dp = [0 for _ in range(n)]

# i 번째 까지 도달 했을 때 얻을 수 있는 최대 개수
# i 번째를 선택하지 않거나
# i 번째를 선택하는 방법

dp[0] = warehouse[0]
dp[1] = max(warehouse[0], warehouse[1])
for i in range(2, n):
    # 만약 i 번째를 선택할 경우
    t1 = warehouse[i] + dp[i-2]

    # 만약 i 번째를 선택하지 않을 경우
    t2 = dp[i-1]
    dp[i] = max(t1, t2)

print(dp[n-1])