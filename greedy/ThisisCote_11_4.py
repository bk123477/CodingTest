import sys
input = sys.stdin.readline

n = int(input().rstrip())
coins = list(map(int, input().rstrip().split()))
coins.sort(reverse=True)

result = 1
# coins = [9,3,2,1,1]
while True:
    temp = result
    for coin in coins:
        if temp >= coin:
            temp -= coin
    if temp != 0:
        break
    else: result += 1

print(result)

# sol) 이렇게 풀어도 될 거 같은데 책의 답이 더 짧음. coins의 원소에 따라 이전 까지는 다 만들 수 있다 가정하고 coins를 target에 더해가며 찾음.

# n = int(input())
# data = list(map(int, input().rstrip().split()))
# data.sort()

# target = 1
# for x in data:
#     if target < x:
#         break
#     target += x

# print(target)