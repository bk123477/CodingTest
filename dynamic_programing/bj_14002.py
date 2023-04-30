# acmicpc.net/problem/14002

import sys
input = sys.stdin.readline

n = int(input())
inputList = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if inputList[i] > inputList[j]: # 원소가 전 원소보다 크면,
            dp[i] = max(dp[i], dp[j]+1)
            # 전의 원소의 최장 수열 길이+1 과 저장된 수열 길이 값  비교해서 큰 값  대입.
print(max(dp))

sub = [] # 정답 입력
order = max(dp) # max(dp)값 저장
for i in range(n-1, -1, -1): # 뒤에서부터
    if dp[i] == order: # dp[i] 값이 order값과 같다면
        sub.append(inputList[i]) # sub에 추가
        order -= 1 # order 값 감소
sub.reverse()
print(*sub)