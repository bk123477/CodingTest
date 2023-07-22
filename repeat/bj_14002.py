# acmicpc.net/problem/14002

import sys
input = sys.stdin.readline

n = int(input())
input_list = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if input_list[i] > input_list[j]: # 원소가 전 원소보다 크면,
            dp[i] = max(dp[i], dp[j]+1)
            # 전의 원소의 최장 수열 길이+1 과 저장된 수열 길이 값  비교해서 큰 값  대입.
print(max(dp))

sub = []
order = max(dp)
for i in range(n-1, -1, -1):
    if dp[i] == order:
        sub.append(input_list[i])
        order -= 1
sub.reverse()
print(*sub)