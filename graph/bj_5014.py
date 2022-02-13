import sys
from collections import deque
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
move = [u, -d] # bfs 탐색하기 위한 리스트

def bfs():
    queue = deque([s]) # 시작층은 s
    floor = [-1] * (f+1)
    floor[s] = 0
    while queue:
        current = queue.popleft()
        if current == g: # 현재 위치가 g라면 while문 탈출
            break
        for i in move:
            next = current + i
            if 0<next<=f and floor[next] == -1: # 범위 안에 있고, 아직 탐색하지 않은 층
                floor[next] = floor[current] + 1
                queue.append(next)
    if floor[g] == -1:
        print('use the stairs')
    else: print(floor[g])
bfs()