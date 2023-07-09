# acmicpc.net/problem/1339

import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
alphabet = defaultdict(int)
dictionary = []
for _ in range(N):
    temp = input().rstrip()
    dictionary.append(temp)
    for i in range(len(temp)):
        alphabet[temp[i]] += 10**(len(temp) - (i+1))

list_alphabet = list(sorted(alphabet.items(), key=lambda x:x[1], reverse=True))
final_alphabet = []
for alpha in list_alphabet:
    final_alphabet.append(alpha[0])

result = 0
for word in dictionary:
    for i in range(len(word)):
        for j in range(len(final_alphabet)):
            if word[i] == final_alphabet[j]:
                result += (10**(len(word)-(i+1))) * (9-j)

print(result)