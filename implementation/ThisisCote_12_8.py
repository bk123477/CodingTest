import sys
input = sys.stdin.readline

string = input().rstrip()

alphaString = []
numString = 0

for i in range(len(string)):
    if string[i]>='0' and string[i]<='9':
        numString += int(string[i])
    else:
        alphaString.append(string[i])

alphaString.sort()
result = ""
for i in alphaString:
    result += i

if numString == 0: print(result)
else: print(result+str(numString))

# sol)
# 숫자만 있을 경우, 문자만 있을 경우 생각하기
# isalpha() 사용 하기
# 리스트를 문자열로 변환하여 출력하는 것 ''.join(result) 생각 하기

# for x in string:
#     if x.isalpha(): alphaString.append(x)
#     else: numString += int(x)

# alphaString.sort()
# if numString != 0:
#     alphaString.append(str(numString))

# print(''.join(alphaString))