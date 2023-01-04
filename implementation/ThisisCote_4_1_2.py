import sys
input = sys.stdin.readline

n = int(input().rstrip())

result = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                result += 1

print(result)

# 3중 반복문 안의 in 저렇게 사용할 수 있는 것 염두.