def solution(s):
    answer = 0
    simulations = []

    for _ in range(len(s)):
        s_list = list(s)
        s_list.append(s_list[0])
        s_list.pop(0)
        s = ''.join(s_list)
        simulations.append(s)

    for i in range(len(simulations)):
        stack = []
        target = list(simulations[i])
        is_correct = True
        for t in target:
            if t == '(' or t == '[' or t == '{':
                stack.append(t)
            else:
                if len(stack) == 0:
                    is_correct = False
                    break
                elif t == ')' and stack[-1] == '(':
                    stack.pop()
                elif t == ']' and stack[-1] == '[':
                    stack.pop()
                elif t == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    is_not_correct = False
                    break

        if len(stack) == 0 and is_correct:
            answer += 1

    return answer
