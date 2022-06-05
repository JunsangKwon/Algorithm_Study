import sys

input = sys.stdin.readline

r, c = map(int, input().split())
image = [list(input()) for _ in range(r)]
result = [['.'] * c for _ in range(r)]
move = 3001

for i in range(c):
    max_star = 0
    min_ground = 3001
    flag = False

    for j in range(r):
        if image[j][i] == 'X':
            if max_star < j:
                max_star = j
            flag = True

        if image[j][i] == '#':
            if min_ground > j:
                min_ground = j

    if flag and move > min_ground - max_star - 1:
        move = min_ground - max_star - 1


for i in range(r):
    for j in range(c):
        if image[i][j] == 'X':
            result[i + move][j] = 'X'
        elif image[i][j] == '#':
            result[i][j] = '#'

for i in range(r):
    for j in range(c):
        sys.stdout.write(result[i][j])
    sys.stdout.write('\n')
