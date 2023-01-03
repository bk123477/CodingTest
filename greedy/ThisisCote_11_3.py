import sys
input = sys.stdin.readline

S = input().rstrip()
result = 0

count0 = count1 = 0

# 맨 처음 처리
if S[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(S) - 1):
    if S[i] != S[i+1]:
        if S[i+1] == '1': count0 += 1
        else: count1 += 1

print(min(count0, count1))

# sol)
# count0, 1은 각각 전부 0으로 바꾸기, 전부 1로 바꾸기
# 문자열 전체를 돌면서 다음번 원소와 숫자가 다를 때
# 바꿔야 할 원소 count에 기록