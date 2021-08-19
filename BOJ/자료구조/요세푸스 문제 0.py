from sys import stdin
from collections import deque

queue = deque()
n, k = map(int, stdin.readline().split())
answer = []
count = 0

for i in range(n):
    queue.append(str(i+1))

while(queue):
    count += 1
    if(count != k):
        queue.append(queue[0])
        queue.popleft()
    else:
        answer.append(queue[0])
        queue.popleft()
        count = 0

print("<%s>" % (", ".join(answer)))
