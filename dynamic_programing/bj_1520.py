# acmicpc.net/problem/1520

import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

m, n = map(int, input().split())
roadMap = []
for _ in range(m):
    tempList = list(map(int, input().split()))
    roadMap.append(tempList)

dpTable = [[-1] * n for _ in range(m)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x, y):
    if x == m-1 and y == n-1: # 도착
        return 1
    if dpTable[x][y] != -1: # 이미 방문하였음
        return dpTable[x][y]
    
    way = 0
    for i in range(4): # 네 방향 탐색하면서 현재 위치보다 더 낮은 곳이 있다면 그곳의 경우의 수를 더해줌.
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<m and 0<=ny<n and roadMap[nx][ny] < roadMap[x][y]:
            way += dfs(nx, ny)
    
    dpTable[x][y] = way
    return dpTable[x][y]

print(dfs(0,0))