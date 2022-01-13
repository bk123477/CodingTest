l, p = map(int, input().split())

people = l * p
data = list(map(int, input().split()))
result = [0] * 5
for i in range(5):
    result[i] = data[i] - people
    print(result[i], end=' ')