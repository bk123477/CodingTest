# acmicpc.net/problem/2470

import sys
input = sys.stdin.readline

N = int(input())

liquid = list(map(int, input().split()))
liquid.sort()

result = []
left_idx = 0
right_idx = N-1
answer = 2e9 + 1

while left_idx < right_idx:
    left = liquid[left_idx]
    right = liquid[right_idx]
    ans = left+right
    if abs(ans) < answer:
        answer = abs(ans)
        result = [liquid[left_idx], liquid[right_idx]]
    
    if ans == 0:
        break
    elif ans < 0:
        left_idx += 1
    else:
        right_idx -= 1

print(result[0], result[1])