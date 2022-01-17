import sys

n = int(sys.stdin.readline().rstrip())
dict1 = {}
for _ in range(n):
    book_name = sys.stdin.readline().rstrip()
    dict1[book_name] = dict1.setdefault(book_name, 0) + 1
book_list, book_sell = [], []
for i, j in dict1.items():
    book_list.append(i)
    book_sell.append(j)
max_book = book_list[0]
max_cnt = 0
for i in range(len(book_sell)):
    if book_sell[i] > max_cnt:
        max_cnt = book_sell[i]
        max_book = book_list[i]
    elif book_sell[i] == max_cnt:
        if book_list[i] < max_book:
            max_cnt = book_sell[i]
            max_book = book_list[i]
print(max_book)