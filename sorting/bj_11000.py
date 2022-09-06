import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
arr = []
for _ in range(n):
    a, b = map(int, input().split(' '))
    arr.append([a,b])

arr.sort()

room = []
heapq.heappush(room, arr[0][1]) # 첫 번째 애의 끝나는 시간 넣어줌

for i in range(1, n):
    if arr[i][0] < room[0]: # 끝나는 시간이 다음애의 시작시간 보다 늦은경우
        heapq.heappush(room, arr[i][1]) # 힙큐에 넣어줌
    else: # 수업 바로 깔 수 있을 경우
        heapq.heappop(room) # 이전 애를 제거하고
        heapq.heappush(room, arr[i][1]) # 새로운 애로 강의 박음

print(len(room))