import sys

string = list(sys.stdin.readline().rstrip())
search = list(sys.stdin.readline().rstrip())

number = 0        
index = 0
while True:
    if index + len(search) > len(string):
        break
    if search == string[index:index+len(search)]:
        number += 1
        index += len(search)
    else:
        index += 1

print(number)