from collections import deque


def solution(priorities, location):
    queue = deque(priorities)
    indexqueue = deque()
    answer = 0
    printed = []

    for i in range(len(priorities)):
        indexqueue.append(i)

    while(queue):
        if(queue[0] != max(queue)):
            tmp = queue[0]
            tmpIndex = indexqueue[0]
            queue.popleft()
            indexqueue.popleft()
            queue.append(tmp)
            indexqueue.append(tmpIndex)
        else:
            queue.popleft()
            printed.append(indexqueue[0])
            indexqueue.popleft()

    for i in range(len(printed)):
        if(printed[i] == location):
            answer = i+1

    return answer
