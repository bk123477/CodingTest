import sys
input = sys.stdin.readline

n = int(input().rstrip()) # 저울추의 개수
arr = list(map(int, input().split(' ')))
arr.sort() # 정렬 되어 있음

last_int = 0 # 지금까지의 더한 모든 수의 합(여기까진 찾을 수 있음)

for i in range(n): # 배열 순서대로 탐색하면서
    left_int = 0 + arr[i] # 이번에 추가된 수의 왼쪽 범위
    right_int = last_int + arr[i] # 이번에 추가된 수의 오른쪽 범위

    if last_int+1 < left_int: # 연결이 되지 않는 경우 = 못찾는 경우
        break
    else: # 다음범위 탐색
        last_int = right_int

print(last_int + 1)