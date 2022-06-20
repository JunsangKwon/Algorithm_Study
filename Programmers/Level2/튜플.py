from collections import Counter


def solution(s):
    answer = []
    s = s[2:-2]
    second = []
    third = []
    num_list = []

    first = s.split(',')

    for tup in first:
        second += tup.split('{')

    for tup in second:
        third += tup.split('}')

    for i in range(len(third)):
        if third[i] != '':
            num_list.append(third[i])

    order = Counter(num_list).most_common()

    for i in range(len(order)):
        answer.append(int(order[i][0]))

    return answer
