from itertools import permutations


def solution(k, dungeons):
    answer = []
    dun_length = len(dungeons)
    orders = [i for i in range(dun_length)]
    per = list(permutations(orders, dun_length))

    for i in range(len(per)):
        piro = k
        count = 0
        order = per[i]
        for j in range(len(order)):
            if piro < dungeons[order[j]][0]:
                break
            else:
                piro -= dungeons[order[j]][1]
                count += 1
        answer.append(count)

    return max(answer)
