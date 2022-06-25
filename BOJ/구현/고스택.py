print_list = []


while True:
    program = []
    nums = []

    break_flag = False
    while True:
        operator = list(map(str, input().split()))
        if operator[0] == 'END':
            break
        elif operator[0] == 'QUIT':
            break_flag = True
            break
        else:
            program.append(operator)

    if break_flag:
        break

    n = int(input())
    for i in range(n):
        nums.append(int(input()))

    for i in range(n):
        stack = [nums[i]]
        for j in range(len(program)):
            if program[j][0] == 'NUM':
                stack.append(int(program[j][1]))
            elif program[j][0] == 'POP':
                if len(stack) == 0:
                    break
                stack.pop()
            elif program[j][0] == 'INV':
                if len(stack) == 0:
                    break
                top_value = stack.pop() * (-1)
                stack.append(top_value)
            elif program[j][0] == 'DUP':
                if len(stack) == 0:
                    break
                stack.append(stack[-1])
            elif program[j][0] == 'SWP':
                if len(stack) < 2:
                    stack.clear()
                    break
                first = stack.pop()
                second = stack.pop()
                first, second = second, first
                stack.append(second)
                stack.append(first)
            elif program[j][0] == 'ADD':
                if len(stack) < 2:
                    stack.clear()
                    break
                first = stack.pop()
                second = stack.pop()
                new = first + second
                stack.append(new)
            elif program[j][0] == 'SUB':
                if len(stack) < 2:
                    stack.clear()
                    break
                first = stack.pop()
                second = stack.pop()
                new = second - first
                stack.append(new)
            elif program[j][0] == 'MUL':
                if len(stack) < 2:
                    stack.clear()
                    break
                first = stack.pop()
                second = stack.pop()
                new = first * second
                stack.append(new)
            elif program[j][0] == 'DIV':
                first_sign = 1
                second_sign = 1
                if len(stack) < 2:
                    stack.clear()
                    break
                first = stack.pop()
                second = stack.pop()
                if first == 0:
                    stack.clear()
                    break
                elif first < 0:
                    first_sign = -1
                    first = abs(first)

                if second < 0:
                    second_sign = -1
                    second = abs(second)

                new = second // first
                new = new * first_sign * second_sign
                stack.append(new)
            elif program[j][0] == 'MOD':
                second_sign = 1
                if len(stack) < 2:
                    stack.clear()
                    break
                first = stack.pop()
                second = stack.pop()
                if first == 0:
                    stack.clear()
                    break
                elif first < 0:
                    first = abs(first)

                if second < 0:
                    second_sign = -1
                    second = abs(second)

                new = second % first
                new = new * second_sign
                stack.append(new)
        if len(stack) != 1:
            print_list.append('ERROR')
            stack.clear()
        else:
            if abs(stack[-1]) > 1000000000:
                print_list.append('ERROR')
                stack.clear()
            else:
                print_list.append(stack[-1])
                stack.clear()

    print_list.append(' ')
    s = input()

for i in range(len(print_list)):
    if print_list == ' ':
        print()
    else:
        print(print_list[i])
