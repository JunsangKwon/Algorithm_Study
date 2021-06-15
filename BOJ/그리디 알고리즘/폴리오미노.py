import sys

words = list(map(str, sys.stdin.readline().strip()))
transwords = []
numOfX = []
indexOfdot = []
count = 0

for i in words:
    if(i == 'X'):
        count += 1

    elif(i == '.'):
        if(count != 0):
            numOfX.append(count)
        count = 0
if(count != 0):
    numOfX.append(count)

for i in range(len(words)):
    if(words[i] == '.'):
        indexOfdot.append(i)

for i in numOfX:
    if(i % 2 == 1):
        print(-1)
        exit()
    elif(i % 4 == 0):
        transwords += list('A' * i)
    else:
        transwords += list('A' * (i-2) + 'B' * 2)

for i in indexOfdot:
    transwords.insert(i, '.')

for i in transwords:
    print(i, end="")
