import sys

n = int(sys.stdin.readline().strip())
wh = []
answers = [0]*n

for i in range(n):
    weight, height = (map(int, sys.stdin.readline().strip().split()))
    wh.append([weight, height, i])

rank = sorted(wh, key=lambda x: x[0], reverse=True)
mainrank = [0]*n

for i in range(n):
    mainrank[i] = rank[i][1]

restrank = mainrank
ranking = 1
tmprank = 0

for i in range(n):
    if(mainrank[i] == max(mainrank)):
        answers[rank[i][2]] = ranking
        mainrank[i] = 0
        ranking += 1
        if(tmprank != 0):
            ranking += tmprank
            tmprank = 0

    else:
        answers[rank[i][2]] = ranking
        mainrank[i] = 0
        tmprank += 1

for i in answers:
    print(i, end=" ")
