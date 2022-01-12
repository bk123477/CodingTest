import sys

n, m = map(int, sys.stdin.readline().split())

if(n<m):
     print(m-n)
else:
    print(n-m)