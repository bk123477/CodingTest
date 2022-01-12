import sys
n = int(input())
f = int(input())

hundred = n - n%100
new_num = hundred
while True:
    if(new_num % f == 0):
        break
    new_num += 1

result = new_num - hundred
print("%02d" % result) #print 0