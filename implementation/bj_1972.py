import sys

result = []
while True:
    string = sys.stdin.readline().rstrip()
    if string == '*':
        break
    else:
        if len(string) == 1:
           result.append(string + " is surprising.") 
        else: # len(string) is 2 ~
            flag = 0       
            for i in range(len(string) - 1): # 0쌍부터 N-2쌍까지
                dict1 = {}
                for j in range(len(string) - (i + 1)): # D-쌍 생성 잘 됨.
                    temp = string[j] + string[j+i+1]
                    dict1[temp] = dict1.setdefault(temp, 0) + 1
                for v in dict1.values():
                    if v != 1:
                        flag = -1
                if flag == -1:
                    result.append(string + " is NOT surprising.")
                    break
            if flag == 0:
                result.append(string + " is surprising.")
for s in result:
    print(s)