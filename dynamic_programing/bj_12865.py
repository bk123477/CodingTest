import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # N = 물품 수, K = 버틸 수 있는 무게

nList = [[0,0]]
dp = [[0]*(K+1) for _ in range(N+1)]

for _ in range(N):
    nList.append(list(map(int, input().split())))

for i in range(1, N+1): # i = 물건 개수 도는 index
    for j in range(1, K+1): # j = 배낭 무게 도는 index
        w = nList[i][0]
        v = nList[i][1]

        # 현재 배낭의 허용 무게보다 넣을 무게가 큰 경우(못 넣는 경우)
        if j < w:
            # 이전의 무게 그대로 가져옴
            dp[i][j] = dp[i-1][j]
        # 현재 배낭의 허용 무게가 넣을 물건의 무게를 감당할 수 있을 때
        else:
            # 1. 현재 넣을 물건의 무게를 배낭에서 빼고 현재 물건 넣음
            # 2. 현재 물건 넣지 않고 이전 무게 그대로 가져옴
            # 위 두 경우 중 더 큰 가치를 선택
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[N][K])