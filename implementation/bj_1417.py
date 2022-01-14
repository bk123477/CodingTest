n = int(input())
data = [0] * n
for i in range(n):
    data[i] = int(input())
dasom = data[0]
data[0] = 0
people = 0
while True:
    data.sort(reverse=True)
    if(dasom > data[0]):
        break
    else:
        data[0] -= 1
        dasom += 1
        people += 1
        data.sort(reverse=True)
        
print(people)