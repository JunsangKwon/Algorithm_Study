import sys

n = int(input())

weights = []
heights = []
answer = [0] * n
rank = 1
flag = False
count = 0

for i in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    weights.append([x, i])
    heights.append([y, i])

weights = sorted(weights, key=lambda x: x[0], reverse=True)
heights = sorted(heights, key=lambda x: x[0], reverse=True)

i = 0
while(i < n):
    j = i
    if(weights[i][1] == heights[i][1]):
        answer[weights[i][1]] = rank
        rank += 1
        i += 1
        continue

    while(weights[i][1] != heights[j][1]):
        flag = True
        answer[heights[j][1]] = rank
        j += 1
        count += 1
        if(j >= n):
            flag = False
            break

    if(flag):
        answer[weights[i][1]] = rank
        rank += count+1

        i = j+1
        flag = False
        count = 0

for k in answer:
    print(k, end=" ")
