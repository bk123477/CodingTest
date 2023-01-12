# acmicpc.net/problem/18310
# 못 풂...

import sys
input = sys.stdin.readline

n = int(input().rstrip())
houseList = list(map(int, input().rstrip().split()))
houseList.sort()

print(houseList[(n-1)//2])