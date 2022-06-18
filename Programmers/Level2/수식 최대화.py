from itertools import permutations


def solution(expression):
    answer = 0
    priority = list(permutations(['+', '-', '*'], 3))
    candidates = []

    for i in range(len(priority)):
        first = expression.split(priority[i][0])
        new = []
        for ex in first:
            second = ex.split(priority[i][1])
            second = [str(eval(x)) for x in second]
            new.append(priority[i][1].join(second))

        new = [str(eval(x)) for x in new]
        candidates.append(abs(eval(priority[i][0].join(new))))

    return max(candidates)
