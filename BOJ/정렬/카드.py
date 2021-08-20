from collections import Counter
from sys import stdin

cards = []
n = int(stdin.readline())
for i in range(n):
    cards.append(int(stdin.readline()))

frequency = Counter(cards).most_common()
frequency.sort(key=lambda x: (-x[1], x[0]))
print(frequency[0][0])
