import sys

n = int(sys.stdin.readline().rstrip())
a = [0] * 1000001
a[1] = 0
a[2] = 1
a[3] = 1
# 1빼기, 3으로나누기, 2로 나누기 뭐가 더 최소일지 모름!!!!! 세가지 케이스 다 해봐야함...
for i in range(4, n+1):
    a[i] = a[i-1] + 1
    if i % 3 == 0:
        a[i] = min(a[i], a[i//3] + 1) 
    if i % 2 == 0:
        a[i] = min(a[i], a[i//2] + 1)
print(a[n])