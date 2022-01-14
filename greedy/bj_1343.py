import sys
data = list(sys.stdin.readline().rstrip())
result = []
sum = 0
flag = 0
for i in range(len(data)):
    if(data[i] == 'X'):
        sum += 1
    else: # 지금까지 누적된 보드판 덮기 == data[i] is '.'
        if (sum % 2) != 0: # 홀수
            flag = 1
            break
        else:
            result += 'AAAA' * (sum//4) + 'BB' * (sum%4 - 1) + '.'
            sum = 0
if sum > 0:
    if(sum % 2) != 0:
        flag = 1
    else:
        result += 'AAAA' * (sum//4) + 'BB' * ((sum-4*(sum//4))//2)

if flag == 1:
    print(-1)
else:
    print(''.join(result))