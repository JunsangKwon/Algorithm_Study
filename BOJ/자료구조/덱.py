from collections import deque
from sys import stdin

deq = deque()
commands = []
answer = []


def push_back(value):
    deq.append(value)


def push_front(value):
    deq.appendleft(value)


def pop_front():
    if(deq):
        answer.append(deq.popleft())
    else:
        answer.append(-1)


def pop_back():
    if(deq):
        answer.append(deq.pop())
    else:
        answer.append(-1)


def front():
    if(deq):
        answer.append(deq[0])
    else:
        answer.append(-1)


def back():
    if(deq):
        answer.append(deq[-1])
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
    if(commands[i][0] == "push_back"):
        push_back(int(commands[i][1]))
    elif(commands[i][0] == "push_front"):
        push_front(int(commands[i][1]))
    elif(commands[i][0] == "pop_front"):
        pop_front()
    elif(commands[i][0] == "pop_back"):
        pop_back()
    elif(commands[i][0] == "size"):
        size()
    elif(commands[i][0] == "empty"):
        empty()
    elif(commands[i][0] == "front"):
        front()
    elif(commands[i][0] == "back"):
        back()

for i in range(len(answer)):
    print(answer[i])
