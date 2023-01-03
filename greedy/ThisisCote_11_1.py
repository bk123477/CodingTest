import sys
input = sys.stdin.readline

n = int(input().rstrip())
horror = list(map(int, input().rstrip().split()))
horror.sort()

result = count = 0

for i in horror:
    count += 1
    if count >= i: # 현재 공포도보다 그룹 인원수가 크거나 같으면 바로 그룹 결성
        result += 1
        count = 0

print(result)

# sol)
# 내림차순으로 풀었었는데, 오름차순으로 풀어야 함.