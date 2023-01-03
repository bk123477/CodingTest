import sys
input = sys.stdin.readline

S = input().rstrip()

result = int(S[0])

for i in range(1,len(S)):
    second = int(S[i])
    if result <=1 or second <= 1:
        result += second
    else:
        result *= second

print(result)

# sol)
# 두 연산자가 0 혹은 1일 경우에는 더하기를 수행하여야 함.
# 1일때 경우 놓치지 않기.