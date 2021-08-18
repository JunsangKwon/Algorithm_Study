from collections import deque
from sys import stdin

answer = []
t = int(stdin.readline())


for i in range(t):
    n, index = map(int, stdin.readline().split())
    count = 0
    priority = list(map(int, stdin.readline().split()))
    indexList = []
    queue = deque(priority)

    for i in range(n):
        indexList.append(i)
    indexQueue = deque(indexList)

    while(queue):
        if(queue[0] != max(queue)):
            queue.append(queue[0])
            queue.popleft()
            indexQueue.append(indexQueue[0])
            indexQueue.popleft()
        else:
            if(indexQueue[0] == index):
                count += 1
                answer.append(count)
                break
            else:
                queue.popleft()
                indexQueue.popleft()
                count += 1

for a in answer:
    print(a)
