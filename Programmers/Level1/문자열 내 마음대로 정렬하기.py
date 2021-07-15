def solution(strings, n):
    answer = []
    with_keyword = []
    for i in range(len(strings)):
        with_keyword.append([strings[i], strings[i][n]])

    with_keyword = sorted(with_keyword, key=lambda x: (x[1], x[0]))

    for i in with_keyword:
        answer.append(i[0])
    return answer
