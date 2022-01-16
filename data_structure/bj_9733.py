import sys

li = []
for i in range(24):
    k = list(sys.stdin.readline().rstrip().split())
    if k == []:
        break
    else:
        li += k

total_length = len(li)
# Order : Re, Pt, Cc, Ea, Tb, Cm, Ex
order = [0] * 7
total = 0
for i in range(total_length):
    if li[i] == 'Re':
        order[0] += 1
        total += 1
    elif li[i] == 'Pt':
        order[1] += 1
        total += 1
    elif li[i] == 'Cc':
        order[2] += 1
        total += 1
    elif li[i] == 'Ea':
        order[3] += 1
        total += 1
    elif li[i] == 'Tb':
        order[4] += 1
        total += 1
    elif li[i] == 'Cm':
        order[5] += 1
        total += 1
    elif li[i] == 'Ex':
        order[6] += 1
        total += 1
    else:
        total += 1
print('Re', order[0], "%.2F" %(order[0]/total))
print('Pt', order[1], "%.2F" %(order[1]/total))
print('Cc', order[2], "%.2F" %(order[2]/total))
print('Ea', order[3], "%.2F" %(order[3]/total))
print('Tb', order[4], "%.2F" %(order[4]/total))
print('Cm', order[5], "%.2F" %(order[5]/total))
print('Ex', order[6], "%.2F" %(order[6]/total))
print('Total', total, "%.2F" %(1))