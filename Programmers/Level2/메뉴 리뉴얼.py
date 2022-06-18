from itertools import combinations

def solution(orders, course):
    answer = []

    for x in range(len(course)):
        candidates = []
        word_count = 0
        for y in range(len(orders)):
            if len(orders[y]) >= course[x]:
                word_count += 1
        if word_count < 2:
            break
        
        for y in range(len(orders)):
            order_list = list(orders[y])
            order_list.sort()
            candidates += list(map(''.join, combinations(order_list, course[x])))

        candidates = list(set(list(candidates)))
        candidates.sort()
        counts = [0] * len(candidates)
        for i in range(len(candidates)):
            for j in range(len(orders)):
                tmp_count = 0
                for k in range(len(candidates[i])):
                    if candidates[i][k] in orders[j]:
                        tmp_count += 1
                if tmp_count == len(candidates[i]):
                    counts[i] += 1
        
        max_value = max(counts)
        for i in range(len(counts)):
            if max_value == counts[i] and counts[i] >= 2:
                answer.append(candidates[i])

    answer.sort()
    return answer