import sys
data = list(map(int, sys.stdin.readline().rstrip().split())) # in list, x, y, w, h store
xdiffer = data[2] - data[0]
ydiffer = data[3] - data[1]

if(data[0] < xdiffer):
    xdiffer = data[0]
if(data[1] < ydiffer):
    ydiffer = data[1]

if(xdiffer < ydiffer):
    print(xdiffer)
else:
    print(ydiffer)