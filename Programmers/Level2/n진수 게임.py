n_dic = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
}


def change(num, n):
    result = ''

    q, r = divmod(num, n)

    while q > 0:
        result = result + n_dic[r]
        q, r = divmod(q, n)

    result = result + n_dic[r]

    return result[::-1]


def solution(n, t, m, p):
    answer = ''
    game_record = ''
    repeat_num = m * t
    for i in range(repeat_num):
        game_record += change(i, n)

    for i in range(t):
        answer += game_record[m*i + (p - 1)]

    return answer
