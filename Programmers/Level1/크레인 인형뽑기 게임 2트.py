def solution(board, moves):
    answer = 0
    n = len(board)
    bucket = []

    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] == 0:
                continue
            else:
                bucket.append(board[i][m-1])
                board[i][m-1] = 0
                break

        if len(bucket) > 1 and bucket[-1] == bucket[-2]:
            bucket.pop()
            bucket.pop()
            answer += 2

    return answer
