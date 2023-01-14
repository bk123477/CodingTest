# 굳이 transpose 과정 없어도 됨.
# 이렇게 해도 시간초과 안 날까?

import sys
input = sys.stdin.readline

t = int(input().rstrip())

def Testcase():
    n, m = map(int, input().rstrip().split())
    goldMapTranspose = []
    totalInfo = list(map(int, input().rstrip().split()))
    for i in range(m):
        tempList = []
        for j in range(n):
            tempList.append(totalInfo[m*j + i])
        goldMapTranspose.append(tempList)
    for i in range(1,m):
        for j in range(n):
            if j == 0:
                goldMapTranspose[i][j] = goldMapTranspose[i][j] + max(goldMapTranspose[i-1][j], goldMapTranspose[i-1][j+1])
            elif j == n-1:
                goldMapTranspose[i][j] = goldMapTranspose[i][j] + max(goldMapTranspose[i-1][j], goldMapTranspose[i-1][j-1])
            else:
                goldMapTranspose[i][j] = goldMapTranspose[i][j] + max(goldMapTranspose[i-1][j], goldMapTranspose[i-1][j-1], goldMapTranspose[i-1][j+1])
    print(max(goldMapTranspose[m-1]))
    

for _ in range(t):
    Testcase()