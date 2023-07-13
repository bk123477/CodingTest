# acmicpc.net/problem/2110

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

start = 1  # 최소 거리
end = arr[-1] - arr[0] # 최대 거리
result = 0

while start <= end:
    mid = (start + end) // 2
    cursor = arr[0]
    cnt = 1
    for i in range(1, len(arr)):
        if arr[i] >= cursor + mid: # 두 번째 값이 시작값 + 거리보다 크면
            cursor = arr[i]
            cnt += 1
    if cnt >= C: # 개수가 공유기 개수보다 많으면 차이 키워줌
        start = mid + 1
        result = mid
    else: # 개수가 공유기보다 적게 설치되면 차이 줄이기
        end = mid - 1

print(result)