n, m = map(int, input().split())
data = [0] * m
best = 0
price = 0
for i in range(m):
    data[i] = int(input())
data.sort(reverse=True)

for i in range(m):
    sum = 0
    if n < i+1:
        sum = data[i] * n
    else:
        sum = data[i] * (i + 1)
    
    if best < sum:
        price = data[i]
        best = sum
    
print(price, best)