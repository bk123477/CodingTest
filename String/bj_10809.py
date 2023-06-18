import sys
input = sys.stdin.readline

string = input().rstrip()
alphabet = [-1] * 26

for i in range(len(string)):
    temp = ord(string[i])-97
    if alphabet[temp] == -1:
        alphabet[temp] = i
    
for a in alphabet:
    print(a, end=" ")