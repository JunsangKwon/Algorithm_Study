def divide(p):
    left_count = 0
    right_count = 0
    u = ''
    v = ''
    for i in range(len(p)):
        if p[i] == '(':
            left_count += 1
        else:
            right_count += 1

        if left_count != 0 and left_count == right_count:
            u = p[:i+1]
            v = p[i+1:]
            break

    return u, v


def determine(u):
    stack = []
    is_invalid = False
    for i in range(len(u)):
        if u[i] == '(':
            stack.append(0)
        else:
            if len(stack) == 0:
                is_invalid = True
                break
            else:
                stack.pop()

    if len(stack) == 0 and not is_invalid:
        return True
    else:
        return False


def solution(p):
    if p == '':
        return ''

    u, v = divide(p)

    if determine(u):
        return u + solution(v)

    else:
        new_str = '(' + solution(v) + ')'

        for i in range(len(u)):
            if i == 0 or i == len(u) - 1:
                continue
            else:
                if u[i] == '(':
                    new_str += ')'
                else:
                    new_str += '('

    return new_str
