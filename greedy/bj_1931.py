import sys
input = sys.stdin.readline

total_num = int(input().rstrip())
time_table = [list(map(int, input().rstrip().split())) for _ in range(total_num)] #시작시간, 끝나는 시간

time_table.sort(key = lambda x:(x[1], x[0])) #1순위 끝나는 시간, 2순위 시작 시간 순으로 오름차순 정렬

cnt = 0 # 토탈 카운트(답)
latest = -1 # 가장 최신 회의
# print(time_table)

for i in time_table:
    if latest <= i[0]: # 가장 최신회의보다 늦게 시작하는 가장 빠른 회의 발견할 경우
        cnt+=1
        latest = i[1] # 가장 최신회의 갱신

print(cnt)