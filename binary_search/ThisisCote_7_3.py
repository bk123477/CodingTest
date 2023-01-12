# 파라메트릭 서치 문제. 최적화 문제를 결정 문제로 바꾸어 해결하기.

import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
riceCakeList = list(map(int, input().rstrip().split()))
riceCakeList.sort()
h = riceCakeList[len(riceCakeList) // 2] # 중간값

result = 0
start = 0
end = riceCakeList[len(riceCakeList)-1]

while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in riceCakeList:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else: # 떡의 양이 충분한 경우 덜 자르기
        result = mid # 최대한 덜 자르기가 정답이므로 result에 기록 해두기.
        start = mid + 1

print(result)