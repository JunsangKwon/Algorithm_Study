from collections import deque


def rotation(x1, y1, x2, y2, board):
    q = deque()
    for i in range(y1, y2):
        q.append(board[x1][i])
    for i in range(x1, x2):
        q.append(board[i][y2])
    for i in range(y2, y1, -1):
        q.append(board[x2][i])
    for i in range(x2, x1, -1):
        q.append(board[i][y1])

    q.rotate(1)
    value = min(q)

    for i in range(y1, y2):
        board[x1][i] = q.popleft()
    for i in range(x1, x2):
        board[i][y2] = q.popleft()
    for i in range(y2, y1, -1):
        board[x2][i] = q.popleft()
    for i in range(x2, x1, -1):
        board[i][y1] = q.popleft()

    return value


def solution(rows, columns, queries):
    answer = []
    board = []
    count = 1
    for i in range(rows):
        tmp_row = []
        for j in range(columns):
            tmp_row.append(count + j)
        board.append(tmp_row)
        count += columns

    for i in range(len(queries)):
        answer.append(rotation(
            queries[i][0]-1, queries[i][1]-1, queries[i][2]-1, queries[i][3]-1, board))

    return answer
