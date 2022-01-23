import sys
from math import log2

n, kim, lim = map(int, sys.stdin.readline().rstrip().split())
for round in range(1, int(log2(n)+2)):
    if abs(kim-lim) == 1 and min(kim, lim) % 2 ==1:
        print(round)
        break
    kim = (kim+1) // 2
    lim = (lim+1) // 2