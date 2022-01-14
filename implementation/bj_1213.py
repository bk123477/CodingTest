import sys
#chr(숫자), ord(문자) 'A'=65
s = list(sys.stdin.readline().rstrip())
length = len(s)
alpha_number = [0] * 26 # the number of each alphabet
flag = 0 # the number of alphabets with odd numbers
result = ""
s.sort()
for i in range(length):
    alpha_number[ord(s[i])-65] += 1
for i in range(26):
    if (alpha_number[i] % 2) != 0:
        flag += 1

if (length % 2) == 0:
    if(flag != 0): #length is even, but odd alpha
        print("I'm Sorry Hansoo")
    else: # all even
        for i in range(26):
            if alpha_number[i] != 0:
                temp = chr(i+65) * (alpha_number[i]//2)
                result += temp
        k = list(result)
        k.reverse()
        print(result+''.join(k))
else: # length is odd
    if flag > 1:
        print("I'm Sorry Hansoo")
    else:
        for i in range(26):
            if (alpha_number[i]%2) != 0:
               rest = chr(i+65)
            if alpha_number[i] != 0:
                temp = chr(i+65) * (alpha_number[i]//2)
                result += temp
        k = list(result)
        k.reverse()
        print(result+rest+''.join(k))