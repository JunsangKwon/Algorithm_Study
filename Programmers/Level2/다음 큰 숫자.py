def solution(n):
    answer = 0
    bin_n = format(n, 'b')
    one_num = bin_n.count('1')
    index = 1

    while True:
        next_num = n + index
        bin_next = format(next_num, 'b')
        if bin_next.count('1') == one_num:
            answer = n + index
            break
        else:
            index += 1

    return answer
