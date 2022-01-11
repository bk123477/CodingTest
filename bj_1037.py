import sys

cnt = int(sys.stdin.readline().rstrip())

data = list(map(int, sys.stdin.readline().split()))
data.sort()

if(cnt == 1):
    print(data[0]**2)
else:
    print(data[0] * data[cnt-1])