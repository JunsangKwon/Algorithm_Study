import heapq
from sys import stdin

heap = []
answer = []
n = int(stdin.readline())

for i in range(n):
    tmpValue = int(stdin.readline()) * -1
    if(tmpValue == 0):
        if(len(heap) == 0):
            answer.append(0)
            continue
        else:
            answer.append(heapq.heappop(heap) * -1)
            continue
    else:
        heapq.heappush(heap, tmpValue)

for i in answer:
    print(i)
