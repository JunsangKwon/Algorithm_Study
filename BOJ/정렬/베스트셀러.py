from collections import Counter
from sys import stdin

books = []
n = int(stdin.readline())
for i in range(n):
    books.append(input())

frequency = Counter(books).most_common()
frequency.sort(key=lambda x: (-x[1], x[0]))
print(frequency)
