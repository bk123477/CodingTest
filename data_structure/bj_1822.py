import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
a = set(map(int, sys.stdin.readline().rstrip().split()))
b = set(map(int, sys.stdin.readline().rstrip().split()))
li = list(a-b)
li.sort()
if len(li) == 0:
    print(0)
else:
    print(len(li))
    for i in range(len(li)):
        print(li[i], end = " ")