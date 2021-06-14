import sys

cycle = 0
answer = []

while(True):
    useday = 0
    l, p, v = map(int, sys.stdin.readline().strip().split())

    if(l == 0 and p == 0 and v == 0):
        break

    cycle = v // p
    rest = v % p

    useday += cycle * l
    if(rest < l):
        useday += rest
    else:
        useday += l

    answer.append(useday)

for i in range(len(answer)):
    print("Case %d: %d" % (i+1, answer[i]))
