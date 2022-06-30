def solution(dirs):
    answer = 0
    visited = []
    pi = 5
    pj = 5

    for i in range(len(dirs)):
        if dirs[i] == 'U':
            ti = pi - 1
            if ti < 0 or ti >= 11:
                continue
            if [ti, pj, 'U'] not in visited or [ti + 1, pj, 'D'] not in visited:
                answer += 1
                visited.append([ti, pj, 'U'])
                visited.append([ti + 1, pj, 'D'])
            pi = ti
        elif dirs[i] == 'D':
            ti = pi + 1
            if ti < 0 or ti >= 11:
                continue
            if [ti, pj, 'D'] not in visited or [ti - 1, pj, 'U'] not in visited:
                answer += 1
                visited.append([ti, pj, 'D'])
                visited.append([ti - 1, pj, 'U'])
            pi = ti
        elif dirs[i] == 'L':
            tj = pj - 1
            if tj < 0 or tj >= 11:
                continue
            if [pi, tj, 'L'] not in visited or [pi, tj + 1, 'R'] not in visited:
                answer += 1
                visited.append([pi, tj, 'L'])
                visited.append([pi, tj + 1, 'R'])
            pj = tj
        else:
            tj = pj + 1
            if tj < 0 or tj >= 11:
                continue
            if [pi, tj, 'R'] not in visited or [pi, tj - 1, 'L'] not in visited:
                answer += 1
                visited.append([pi, tj, 'R'])
                visited.append([pi, tj - 1, 'L'])
            pj = tj

    return answer
