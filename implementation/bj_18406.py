n = input()

length = len(n)

left, right = 0, 0

for i in range(length/2):
    left += int(n[i])
    right += int(n[length//2+i])

if left == right:
    print("LUCKY")
else:
    print("READY")