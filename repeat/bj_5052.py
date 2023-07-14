# acmicpc.net/problem/5052

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    num_list = [input().rstrip() for _ in range(n)]
    num_list.sort()

    flag = False
    cnt = 0
    while cnt < n-1:
        if num_list[cnt] == num_list[cnt+1][:len(num_list[cnt])]:
            flag = True
            break
        cnt+=1
    
    if flag:
        print("NO")
    else:
        print("YES")