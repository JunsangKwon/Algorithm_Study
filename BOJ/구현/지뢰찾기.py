from collections import deque
n = int(input())

di = [-1, -1, -1, 0, 1, 1, 1, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1]
mine_map = [list(input()) for _ in range(n)]
open_map = [list(input()) for _ in range(n)]
fire_flag = False


def find_mine(i, j):
    count = 0
    for k in range(8):
        ti = i + di[k]
        tj = j + dj[k]
        if ti < 0 or ti >= n or tj < 0 or tj >= n or open_map[ti][tj] != '*':
            continue
        else:
            count += 1

    open_map[i][j] = count


for i in range(n):
    for j in range(n):
        if mine_map[i][j] == '*':
            if open_map[i][j] == 'x':
                fire_flag = True
                open_map[i][j] = '*'
            else:
                open_map[i][j] = '*'

for i in range(n):
    for j in range(n):
        if open_map[i][j] == 'x':
            find_mine(i, j)

if fire_flag:
    for i in range(n):
        for j in range(n):
            print(open_map[i][j], end="")
        print()
else:
    for i in range(n):
        for j in range(n):
            if open_map[i][j] == '*':
                print('.', end="")
            else:
                print(open_map[i][j], end="")
        print()
