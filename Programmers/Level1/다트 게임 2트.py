def solution(dartResult):
    score_list = []
    tmp_score = 0
    is_ten = False
    for i in range(len(dartResult)):
        if is_ten:
            is_ten = False
            continue
        if dartResult[i].isdigit():
            if i != 0:
                score_list.append(tmp_score)
            if dartResult[i] == '1' and dartResult[i+1] == '0':
                is_ten = True
                tmp_score = 10
            else:
                tmp_score = int(dartResult[i])
        elif dartResult[i].isalpha():
            if dartResult[i] == 'D':
                tmp_score = tmp_score ** 2
            elif dartResult[i] == 'T':
                tmp_score = tmp_score ** 3
        else:
            if dartResult[i] == '*':
                if len(score_list) > 0:
                    score_list[-1] *= 2
                    tmp_score *= 2
                else:
                    tmp_score *= 2
            else:
                tmp_score *= -1

    score_list.append(tmp_score)

    return sum(score_list)
