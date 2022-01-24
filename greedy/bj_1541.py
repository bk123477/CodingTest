import sys

string = sys.stdin.readline().rstrip()
num_arr = []
temp = ""
first = ""
flag = 0 # 연속된 + 개수 세기 위해서
for v  in range(len(string)):
    if string[v] != '+' and string[v] != '-':
        temp += string[v]
        continue
    elif string[v] == '+':
        if flag == 0: # 첫 번째 더하기
            flag = 1
            first = int(temp)
            temp = "" # temp초기화
            continue
        else: #두 번째 더하기
            flag = 1
            first = int(first) + int(temp)
            temp = ""
            continue
    else: # -만남
        if flag == 1: # 더하기 이후 빼기
            first = int(first) + int(temp)
            num_arr.append(first)
            flag = 0
            temp = ""
            continue
        else:
            num_arr.append(int(temp))
            temp = ""

if flag == 1: # 더하기로 끝난 상태
    first = int(first) + int(temp)
    num_arr.append(first)
else:  # 빼기로 끝난 상태
    num_arr.append(int(temp))

result = num_arr[0]
if len(num_arr) == 1:
    print(result)
else:
    for i in range(1, len(num_arr)):
        result -= num_arr[i]
    print(result)