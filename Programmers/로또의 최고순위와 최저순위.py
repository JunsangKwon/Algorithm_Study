def solution(lottos, win_nums):
    answer = []
    lottoranking = [6, 6, 5, 4, 3, 2, 1]
    deletenum = 0
    winnum = 0

    for i in range(6):
        if(lottos[i] == 0):
            deletenum += 1
            continue
        if(lottos[i] in win_nums):
            winnum += 1

    answer.append(lottoranking[winnum + deletenum])
    answer.append(lottoranking[winnum])

    return answer
