
2
3
4
5
6
7
8
9
10
11
12
13


def solution(n, a, b):
    answer = 1

    while True:
        if abs(a - b) == 1 and (a + 1) // 2 == (b + 1) // 2:
            break
        a = (a + 1) // 2
        b = (b + 1) // 2
        answer += 1

    return answer
