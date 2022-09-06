import sys

input = sys.stdin.readline

t = int(input().rstrip()) # 테스트 케이스 개수 t

for _ in range(t):
    n = int(input().rstrip()) # 각 테스트 케이스의 전화번호의 수 n
    arr = [input().rstrip() for _ in range(n)]
    arr.sort() # 오름차순으로 정리됨

    flag = False # 비정상 발견하면 바로 탈출
    cnt = 0
    while cnt < n-1:
        if arr[cnt] == arr[cnt+1][:len(arr[cnt])]: # 앞자리만 비교
            flag = True
            break
        cnt+=1

    if flag:
        print("NO")
    else:
        print("YES")