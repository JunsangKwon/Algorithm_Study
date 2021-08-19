from sys import stdin

members = []
n = int(stdin.readline())

for i in range(n):
    info = list(stdin.readline().split())
    members.append(info)

for i in range(n):
    members[i][0] = int(members[i][0])
    members[i].append(i)

members.sort(key=lambda x: (x[0], x[2]))

for i in range(len(members)):
    print(members[i][0], end=" ")
    print(members[i][1], end="\n")
