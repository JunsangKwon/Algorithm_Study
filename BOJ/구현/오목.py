board = [list(map(int, input().split())) for _ in range(19)]
visited = [[False] * 19 for _ in range(19)]
di = [-1, -1, -1, 0, 1, 1, 1, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1]
win = []
ans_coor = []
break_flag = False


def find_rock(ri, rj, index, color):
    i = ri
    j = rj
    rocks = [[i, j]]

    while board[i][j] == color:
        i += di[index]
        j += dj[index]
        if 0 <= i and i < 19 and 0 <= j and j < 19 and board[i][j] == color:
            rocks.append([i, j])
        else:
            break

    if len(rocks) == 5:
        rocks.sort(key=lambda x: x[1])
        fi = rocks[0][0] - di[index]
        fj = rocks[0][1] - dj[index]
        if 0 <= fi and fi < 19 and 0 <= fj and fj < 19:
            if board[fi][fj] == color:
                return False
        ans_coor.append(rocks[0][0] + 1)
        ans_coor.append(rocks[0][1] + 1)
        win.append(color)
        return True
    else:
        return False


for i in range(19):
    for j in range(19):
        if board[i][j] == 0:
            continue
        for index in range(8):
            ti = i + di[index]
            tj = j + dj[index]
            if 0 <= ti and ti < 19 and 0 <= tj and tj < 19 and board[ti][tj] == board[i][j]:
                if find_rock(i, j, index, board[i][j]):
                    break_flag = True
                    break
        if break_flag:
            break
    if break_flag:
        break

if len(win) == 0:
    print(0)
else:
    print(win[0])
    print(ans_coor[0], ans_coor[1])
