def search(bi, bj, board_list, m, n):
    di = [1, 1, 0]
    dj = [0, 1, 1]
    is_valid = True
    coor = []
    for k in range(3):
        ki = bi + di[k]
        kj = bj + dj[k]
        if ki >= m or kj >= n or board_list[ki][kj] != board_list[bi][bj]:
            is_valid = False
            break
    if is_valid:
        coor.append([bi, bj])
        for k in range(3):
            ki = bi + di[k]
            kj = bj + dj[k]
            coor.append([ki, kj])

    return coor


def solution(m, n, board):
    answer = 0
    board_list = []
    vanish_coor = []

    for i in range(m):
        board_list.append(list(board[i]))

    while True:
        for i in range(m):
            for j in range(n):
                if board_list[i][j] != '*':
                    vanish_coor += search(i, j, board_list, m, n)

        if len(vanish_coor) == 0:
            break

        for i in range(len(vanish_coor)):
            board_list[vanish_coor[i][0]][vanish_coor[i][1]] = '*'

        for i in range(n):
            for j in range(m-1, 0, -1):
                if board_list[j][i] == '*' and board_list[j-1][i] != '*':
                    index = j
                    while index <= m - 1 and board_list[index][i] == '*':
                        board_list[index][i], board_list[index -1][i] = board_list[index-1][i], board_list[index][i]
                        index += 1

        vanish_coor.clear()

    for i in range(m):
        for j in range(n):
            if board_list[i][j] == '*':
                answer += 1

    return answer
