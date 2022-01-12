import sys

n = int(sys.stdin.readline().rstrip())
alpha = [0] * 26
result = []

for i in range(n):
    f_name = sys.stdin.readline().rstrip()
    alpha[ord(f_name[0]) - ord('a')] += 1
for i in range(26):
    if(alpha[i] >= 5):
        result.append(chr(i + ord('a')))

if(len(result) == 0):
    print("PREDAJA")
else:
    for i in range(len(result)):
        print(result[i], end='')