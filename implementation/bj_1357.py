import sys
input = sys.stdin.readline

def rev(inp): # inp = str 자료형
    reverse = ''
    for i in range(len(inp)):
        reverse += inp[len(inp)-i-1]
    return reverse

x, y = input().split()

print(int(rev(str((int(rev(x)) + int(rev(y)))))))