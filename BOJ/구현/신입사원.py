import sys

testcase = int(sys.stdin.readline().strip())
answers = []
for _ in range(testcase):
    rankings = []
    defeaters = 0

    n = int(sys.stdin.readline().strip())
    for i in range(n):
        rankings.append(list(map(int, sys.stdin.readline().strip().split())))

    sortrank = sorted(rankings, key=lambda x: x[0])
    mainrank = [0]*n

    for i in range(n):
        mainrank[i] = sortrank[i][1]

    for i in range(n):
        if(i == 0):
            maxvalue = mainrank[i]
            continue
        if(mainrank[i] > maxvalue):
            defeaters += 1
        else:
            maxvalue = mainrank[i]

    answers.append(n-defeaters)

for i in answers:
    print(i)
