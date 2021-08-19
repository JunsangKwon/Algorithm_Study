from collections import deque
from sys import stdin

n = int(stdin.readline())

cards = []
for i in range(1, n+1):
    cards.append(i)

queue = deque(cards)

while(len(queue) != 1):
    queue.popleft()
    queue.append(queue[0])
    queue.popleft()

print(queue[0])
