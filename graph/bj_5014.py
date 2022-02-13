import sys
from collections import deque
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
move = [u, -d]

def bfs():
    queue = deque([s])
    floor = [-1] * (f+1)
    floor[s] = 0
    while queue:
        current = queue.popleft()
        if current == g:
            break
        for i in move:
            next = current + i
            if 0<next<=f and floor[next] == -1:
                floor[next] = floor[current] + 1
                queue.append(next)
    if floor[g] == -1:
        print('use the stairs')
    else: print(floor[g])
bfs()