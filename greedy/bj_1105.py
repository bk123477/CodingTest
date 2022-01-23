import sys

l, r = map(str, sys.stdin.readline().rstrip().split())

if len(l) != len(r):
    print(0)
else:
    cnt = 0
    for i in range(len(l)):
        if l[i] == r[i]:
            if l[i] == '8':
                cnt+=1
        else: # 같은 자릿수에서 8이 아닌게 존재하면 바로 반복문 빠져나옴
            break
    print(cnt)