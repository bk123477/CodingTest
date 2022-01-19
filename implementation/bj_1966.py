import sys
from collections import deque

total_t = int(sys.stdin.readline().rstrip()) # total_t : 총 테스트케이스 개수
result = []
for _ in range(total_t):
    n, m = map(int, sys.stdin.readline().rstrip().split()) # n: 문서 개수, m : 현재 큐에서 몇 번째 인지
    priority = list(map(int, sys.stdin.readline().rstrip().split())) # priority : n개 문서의 중요도 
    priority_queue = deque()
    count = 1 # 몇번째로 출력 되는지
    for i in range(n): # deque안에 (우선순위, 문서 번호) 넣음
        t1 = (priority[i], i)
        priority_queue.append(t1)
    while True:
        flag = 0
        front = priority_queue.popleft()
        for t in priority_queue:
            if front[0] < t[0]:
                priority_queue.append(front)
                flag = -1
                break
        if flag == -1: # 맨 앞이 인쇄 불가능했음
            continue
        else: # 맨 앞이 인쇄 가능한 상태, flag = 0
            if front[1] == m: # 맨 앞이 찾는 문서였다면 result에 몇 번째로 인쇄 됐는지 기록
                result.append(count)
                break
            else:
                count += 1

for i in result:
    print(i)