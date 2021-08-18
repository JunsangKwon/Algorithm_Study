from collections import deque
from sys import stdin

deq = deque()
commands = []
answer = []


def push(value):
    deq.appendleft(value)


def pop():
    if(deq):
        answer.append(deq.popleft())
    else:
        answer.append(-1)


def top():
    if(deq):
        answer.append(deq[0])
    else:
        answer.append(-1)


def size():
    answer.append(len(deq))


def empty():
    if(deq):
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
    elif(commands[i][0] == "top"):
        top()

for a in answer:
    print(a)
