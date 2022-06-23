def solution(s):
    answer = []
    total_zero = 0
    bin_trans = 0

    while s != '1':
        one_count = list(s).count('1')
        zero_count = list(s).count('0')
        s = bin(one_count)[2:]
        bin_trans += 1
        total_zero += zero_count

    answer = [bin_trans, total_zero]
    return answer
