n = int(input())
num_list = []
stack = []
operators = []
index = 0
is_valid = True

for i in range(n):
    num_list.append(int(input()))

for i in range(n):
    if len(stack) > 0:
        if num_list[index] == stack[-1]:
            while len(stack) != 0 and num_list[index] == stack[-1]:
                operators.append('-')
                stack.pop()
                index += 1
            stack.append(i+1)
            operators.append('+')
        elif num_list[index] > stack[-1]:
            stack.append(i+1)
            operators.append('+')
        else:
            is_valid = False
            break
    else:
        stack.append(i+1)
        operators.append('+')


if is_valid:
    for i in range(index, n):
        if num_list[i] != stack[-1]:
            is_valid = False
            break
        else:
            stack.pop()
            operators.append('-')

    if not is_valid or len(stack) != 0 or len(operators) > 2 * n:
        print("NO")
    else:
        for ans in operators:
            print(ans)
else:
    print("NO")
