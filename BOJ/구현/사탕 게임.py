from sys import stdin
from collections import Counter

n = int(input())
candyMap = [list(input()) for _ in range(n)]
maxValues = []
flag1 = False
flag2 = False


def candyScanner(MAP):
    counts = []
    tmpMAP = []
    tmpArray = []
    count = 1
    finalFlag = False

    for i in range(len(MAP)):
        preValue = MAP[i][0]
        for j in range(1, len(MAP)):
            if(MAP[i][j] == preValue):
                count += 1
                finalFlag = True
            else:
                preValue = MAP[i][j]
                counts.append(count)
                count = 1
                finalFlag = False
        if(finalFlag):
            counts.append(count)
            count = 1
            finalFlag = False

    for i in range(len(MAP)):
        preValue = MAP[0][i]
        for j in range(1, len(MAP)):
            if(MAP[j][i] == preValue):
                count += 1
                finalFlag = True
            else:
                preValue = MAP[j][i]
                counts.append(count)
                count = 1
                finalFlag = False
        if(finalFlag):
            counts.append(count)
            count = 1
            finalFlag = False

    return max(counts)


for i in range(n):
    for j in range(n):
        if(i == n-1):
            flag1 = True
        if(j == n-1):
            flag2 = True

        if(not flag1 and candyMap[i][j] != candyMap[i+1][j]):
            candyMap[i][j], candyMap[i+1][j] = candyMap[i+1][j], candyMap[i][j]
            maxValues.append(candyScanner(candyMap))
            candyMap[i][j], candyMap[i+1][j] = candyMap[i+1][j], candyMap[i][j]

        if(not flag2 and candyMap[i][j] != candyMap[i][j+1]):
            candyMap[i][j], candyMap[i][j+1] = candyMap[i][j+1], candyMap[i][j]
            maxValues.append(candyScanner(candyMap))
            candyMap[i][j], candyMap[i][j+1] = candyMap[i][j+1], candyMap[i][j]

        flag1 = False
        flag2 = False

print(max(maxValues))
