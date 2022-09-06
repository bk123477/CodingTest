import sys
input = sys.stdin.readline

n = int(input().rstrip()) # 수열의 크기 n

negative_arr = []
positive_arr = []
one_arr = []

for _ in range(n):
    temp = int(input().rstrip())
    if temp <=0 :
        negative_arr.append(temp)
    elif temp >1 :
        positive_arr.append(temp)
    else:
        one_arr.append(temp)

negative_arr.sort()
positive_arr.sort(reverse=True)


# negative, positive 순서대로 묶어주기(positive는 내림차순)
# 1인 애들은 마지막에 다 더해주기

sum = 0

if len(positive_arr) % 2 == 0:
    for i in range(len(positive_arr)//2):
        sum += positive_arr[2*i] * positive_arr[2*i + 1]
else:
    for i in range(len(positive_arr)//2):
        sum += positive_arr[2*i] * positive_arr[2*i + 1]
    sum += positive_arr[len(positive_arr)-1]

if len(negative_arr) % 2 == 0:
    for i in range(len(negative_arr)//2):
        sum += negative_arr[2*i] * negative_arr[2*i +1]
else:
    for i in range(len(negative_arr)//2):
        sum += negative_arr[2*i] * negative_arr[2*i + 1]
    sum += negative_arr[len(negative_arr)-1]

for _ in range(len(one_arr)):
    sum += 1

print(sum)