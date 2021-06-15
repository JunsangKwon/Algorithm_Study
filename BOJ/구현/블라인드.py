import sys

m, n = map(int, sys.stdin.readline().strip().split())
apartment = [list(map(str, sys.stdin.readline().strip()))for _ in range(5*m+1)]
lineNum = [False] * 4
answer = [0] * 5
blindtype = [0] * 5

for i in range(5*m+1):
    if(apartment[i][0] == "#" and apartment[i][1] == "#"):
        for i in range(len(blindtype)):
            answer[i] += blindtype[i]
        blindtype = [0] * 5
        lineNum[0] = True
        continue
    if(lineNum[0]):
        for k in range(n):
            if(apartment[i][5*k + 1] == "."):
                blindtype[0] += 1
        lineNum[1] = True
        lineNum[0] = False
        continue
    if(lineNum[1]):
        for k in range(n):
            if(apartment[i][5*k + 1] == "."):
                blindtype[1] += 1
        blindtype[1] -= blindtype[0]
        lineNum[2] = True
        lineNum[1] = False
        continue
    if(lineNum[2]):
        for k in range(n):
            if(apartment[i][5*k + 1] == "."):
                blindtype[2] += 1
        blindtype[2] = blindtype[2] - blindtype[1] - blindtype[0]
        lineNum[3] = True
        lineNum[2] = False
        continue
    if(lineNum[3]):
        for k in range(n):
            if(apartment[i][5*k + 1] == "."):
                blindtype[3] += 1
        blindtype[3] = blindtype[3] - \
            (blindtype[2] + blindtype[1] + blindtype[0])
        if(blindtype[0] + blindtype[1] + blindtype[2] + blindtype[3] < n):
            blindtype[4] = n - (blindtype[0] + blindtype[1] +
                                blindtype[2] + blindtype[3])
        lineNum[3] = False
        continue

for i in answer:
    print(i, end=" ")
