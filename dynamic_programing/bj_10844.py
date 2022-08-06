import sys

n = int(sys.stdin.readline().rstrip()) # 구하고자 하는 수 입력 받음

li = [[0 for _ in range(10)] for _ in range(101)] # 2차원 리스트 초기화

# 1의 자리 수를 기준으로 계산
# 각 자리에서 위의 좌우 대각선의 합과 같음
# 1의 자리 수가 0일때와 9일때만 핸들링

for i in range(1,10):
    li[1][i] = 1
for i in range(2,n+1):
    for j in range(10):
        if j==0:
            li[i][j] = li[i-1][j+1]
        elif j==9:
            li[i][j] = li[i-1][j-1]
        else:
            li[i][j] = li[i-1][j-1] + li[i-1][j+1]

print(sum(li[n]) % 1000000000)