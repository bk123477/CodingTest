import sys
import math

d, h, w = map(int, sys.stdin.readline().split())
k = math.sqrt(d*d / (h*h + w*w))

print(int(h*k), int(w*k))