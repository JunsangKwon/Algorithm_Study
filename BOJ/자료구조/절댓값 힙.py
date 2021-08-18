import heapq
from sys import stdin

heap = []
answer = []
n = int(stdin.readline())

for i in range(n):
    tmpValue = int(stdin.readline())
    if(tmpValue == 0):
        if(len(heap) == 0):
            answer.append(0)
            continue
        else:
            answer.append(heapq.heappop(heap))
            continue
    else:
        heapq.heappush(heap, [abs(tmpValue), tmpValue])

for i in range(len(answer)):
    if(answer[i] == 0):
        print(0)
    else:
        print(answer[i][1])
