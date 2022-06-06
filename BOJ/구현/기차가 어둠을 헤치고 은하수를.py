from sys import stdin

input = stdin.readline
n, m = map(int, input().split())
train_set = [[0] * 20 for _ in range(n)]
pass_train_set = []
pass_train = 0

for i in range(m):
    opers = list(map(int, input().split()))
    if opers[0] == 1:
        train_set[opers[1]-1][opers[2]-1] = 1
    elif opers[0] == 2:
        train_set[opers[1]-1][opers[2]-1] = 0
    elif opers[0] == 3:
        for j in range(18, -1, -1):
            train_set[opers[1]-1][j+1] = train_set[opers[1]-1][j]
        train_set[opers[1]-1][0] = 0
    else:
        for j in range(1, 20):
            train_set[opers[1]-1][j-1] = train_set[opers[1]-1][j]
        train_set[opers[1]-1][19] = 0

for i in range(n):
    if train_set[i] in pass_train_set:
        continue
    else:
        pass_train_set.append(train_set[i])
        pass_train += 1

print(train_set)
print(pass_train)
