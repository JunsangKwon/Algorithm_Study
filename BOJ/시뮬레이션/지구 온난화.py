from collections import deque

r, c = map(int, input().split())
nam_sea = [list(input()) for _ in range(r)]
islands = []
answer = []


def search(si, sj):
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    count = 0

    for k in range(4):
        ki = si + di[k]
        kj = sj + dj[k]
        if ki < 0 or kj < 0 or ki >= r or kj >= c or nam_sea[ki][kj] == '.':
            continue
        count += 1

    if count < 2:
        nam_sea[si][sj] = '*'


for i in range(r):
    for j in range(c):
        if nam_sea[i][j] == 'X':
            search(i, j)

for i in range(r):
    for j in range(c):
        if nam_sea[i][j] == '*':
            nam_sea[i][j] = '.'
        elif nam_sea[i][j] == 'X':
            islands.append([i, j])

island_info = list(map(list, zip(*islands)))
cut_row_min = min(island_info[0])
cut_row_max = max(island_info[0])
cut_col_min = min(island_info[1])
cut_col_max = max(island_info[1])

for i in range(r):
    answer.append(nam_sea[i][cut_col_min: cut_col_max + 1])

answer = answer[cut_row_min: cut_row_max + 1]

for i in range(len(answer)):
    print(''.join(answer[i]))
