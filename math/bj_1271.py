import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

print(n//m) # OverflowError solution
print(n%m)