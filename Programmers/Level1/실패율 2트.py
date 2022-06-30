def solution(N, stages):
    fail_info = []
    answer = []
    for i in range(1, N+1):
        stay_count = 0
        clear_count = 0
        for j in range(len(stages)):
            if stages[j] == i:
                stay_count += 1
            if stages[j] >= i:
                clear_count += 1

        if clear_count == 0:
            fail_info.append([0, i])
        else:
            fail_info.append([stay_count / clear_count, i])

    fail_info.sort(key=lambda x: (-x[0], x[1]))

    for i in range(len(fail_info)):
        answer.append(fail_info[i][1])

    return answer
