# acmicpc.net/problem/14502
# 못 풂. 접근 방식부터 이해히보기. 나중에 다시 풀기.

import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
data = []
temp = [[0]*m for _ in range(n)] # 벽을 설치한 뒤 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().rstrip().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# DFS 이용해서 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상하좌우 중에서 바이러스가 퍼질 수 있는 경우
        if nx>=0 and nx < n and ny>=0 and ny<m:
            if temp[nx][ny] == 0:
                # 바이러스 배치하고 다시 재귀적 수행
                temp[nx][ny] = 2
                virus(nx, ny)
def getScore():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0: score += 1
    return score

# DFS 이용해서 울타리 설치하며 매번 안전 영역 크기 계산
def dfs(count):
    global result
    # 울타리 세 개 설치 된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2: virus(i, j)
        result = max(result, getScore())
        return
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)