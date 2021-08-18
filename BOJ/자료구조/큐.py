from collections import deque
from sys import stdin

queue = deque()
commands = []
answer = []


def push(value):
    queue.append(value)


def pop():
    if(queue):
        answer.append(queue.popleft())
    else:
        answer.append(-1)


def front():
    if(queue):
        answer.append(queue[0])
    else:
        answer.append(-1)


def back():
    if(queue):
        answer.append(queue[-1])
    else:
        answer.append(-1)


def size():
    answer.append(len(queue))


def empty():
    if(queue):
        answer.append(0)
    else:
        answer.append(1)


n = int(stdin.readline())

for i in range(n):
    command = list(stdin.readline().split())
    commands.append(command)

for i in range(n):
    if(commands[i][0] == "push"):
        push(int(commands[i][1]))
    elif(commands[i][0] == "pop"):
        pop()
    elif(commands[i][0] == "size"):
        size()
    elif(commands[i][0] == "empty"):
        empty()
    elif(commands[i][0] == "front"):
        front()
    elif(commands[i][0] == "back"):
        back()

for a in answer:
    print(a)
