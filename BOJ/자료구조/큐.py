from collections import deque
from sys import stdin

queue = deque()
answer = []


n = int(stdin.readline())

for i in range(n):
    command = list(stdin.readline().split())
    if(len(command) == 2):
        queue.append(int(command[1]))
        continue
    elif(command[0] == "pop"):
        if(queue):
            answer.append(queue.popleft())
        else:
            answer.append(-1)
        continue
    elif(command[0] == "size"):
        answer.append(len(queue))
        continue
    elif(command[0] == "empty"):
        if(queue):
            answer.append(0)
        else:
            answer.append(1)
        continue
    elif(command[0] == "front"):
        if(queue):
            answer.append(queue[0])
        else:
            answer.append(-1)
        continue
    elif(command[0] == "back"):
        if(queue):
            answer.append(queue[-1])
        else:
            answer.append(-1)
        continue

for a in answer:
    print(a)
