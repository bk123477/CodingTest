import sys
input = sys.stdin.readline

n, d = map(int, input().rstrip().split())
distance = [i for i in range(d+1)]
shortcut = [list(map(int, input().rstrip().split())) for _ in range(n)]
shortcut.sort()
for start, end, dist in shortcut:
    if end > d:
        continue
    if distance[end] > distance[start] + dist:
        distance[end] = distance[start] + dist
        for x in range(end+1, d+1):
            if distance[x] > distance[x-1] + 1:
                distance[x] = distance[x-1] + 1
            else:
                break
print(distance[d])