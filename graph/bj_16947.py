# acmicpc.net/problem/16947
# pypy3로 제출함.. 추후 다시 보기.

import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)

# 순환선 존재하는지 체크 함수(DFS로 구현)
def circular_station(start, idx, cnt):
    global cycle
    # 방문한 역이 2곳 이상 && 현재 역이 시작 역으로 돌아 옴 => 순환선 존재
    if start == idx and cnt >= 2:
        cycle = True
        return
    # 현재 방문역 표시
    visited[idx] = True
    for i in info[idx]:
        # 아직 방문하지 않은 역
        if not visited[i]:
            # 해당 역 추가 및 재귀 호출
            circular_station(start, i, cnt+1)
        # 이미 방문한 역이고 방문 역이 2곳 이상이라면
        elif i == start and cnt >= 2:
            # 방문하는 역 그대로 재귀 호출
            circular_station(start, i, cnt)

# 역과 순환역 사이 거리 확인 함수(BFS로 구현)
def distance_station(): 
    global check
    q = deque()
    for i in range(N):
        # 순환역에 속하는 역은 모두 거리가 0
        if cycle_station[i]:
            check[i] = 0
            q.append(i)
    
    while q:
        now = q.popleft()
        for i in info[now]:
            # 역이 순환선에 포함되지 않는 다면
            if check[i] == -1:
                # 큐에 추가 후 이동거리 구하기
                q.append(i)
                check[i] = check[now] + 1
    
    for i in check:
        print(i, end=' ')

N = int(input())
info = [[] for _ in range(N)]
cycle_station = [False] * N
check = [-1] * N

for _ in range(N):
    a, b = map(int, input().split())
    info[a-1].append(b-1)
    info[b-1].append(a-1)

for i in range(N):
    visited = [False] * N
    cycle = False
    circular_station(i, i, 0)
    if cycle:
        cycle_station[i] = True

distance_station()