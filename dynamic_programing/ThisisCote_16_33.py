# acmicpc.net/problem/14501
# 못 풂. 뒤에서 부터 하는 방식 참고.

import sys
input = sys.stdin.readline

n = int(input().rstrip())
timeTable = [list(map(int, input().rstrip().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1): # 뒤에서부터 계산
    if i + timeTable[i][0] > n: # 범위 넘어가면 N+1일꺼
        dp[i] = dp[i+1]
    # N+1일의 수익과 N + Tn의 수익 중 큰 값    
    else: # 그 다음날 거의 수입 혹은 이번 것 했을 때의 수입
        dp[i] = max(timeTable[i][1] + dp[i + timeTable[i][0]], dp[i+1])

print(dp[0])
