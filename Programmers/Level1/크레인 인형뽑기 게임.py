def solution(board, moves):
    answer = 0
    newboard = [[0]*len(board) for _ in range(len(board))]
    busket = []
    for i in range(len(board)):
        for j in range(len(board)):
            newboard[i][j] = board[j][i]

    for m in moves:
        for i in range(len(newboard[m-1])):
            if(newboard[m-1][i] == 0):
                continue
            else:
                if(busket and newboard[m-1][i] == busket[-1]):
                    del busket[-1]
                    answer += 2
                    newboard[m-1][i] = 0
                    break
                else:
                    busket.append(newboard[m-1][i])
                    newboard[m-1][i] = 0
                    break

    return answer
