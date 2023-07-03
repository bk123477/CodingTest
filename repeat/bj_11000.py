# acmicpc.net/problem/11000

import sys
import heapq
input = sys.stdin.readline

N = int(input())
class_info = []
for _ in range(N):
    si, ti = map(int, input().split())
    class_info.append([si, ti])

class_info.sort(key=lambda x:(x[0], x[1]))

classroom = []
heapq.heappush(classroom, class_info[0][1])

for i in range(1, N):
    if class_info[i][0] < classroom[0]: # 새로운 강의실 배정해야함.
        heapq.heappush(classroom, class_info[i][1])
    else:
        heapq.heappop(classroom)
        heapq.heappush(classroom, class_info[i][1])

print(len(classroom))