import sys
input = sys.stdin.readline

n = int(input().rstrip())

string = str(n)
left = right = 0

for i in range(len(string)//2):
    left += int(string[i])
    right += int(string[len(string)//2 + i])

if left == right: print("LUCKY")
else: print("READY")
