alpha_dic = {}
n = int(input())
expression = list(input())
stack = []

for e in expression:
    if e.isalpha():
        alpha_dic[e] = 0

for i in range(n):
    alpha_dic[chr(i + 65)] = input()

for i in range(len(expression)):
    if expression[i].isalpha():
        expression[i] = alpha_dic[expression[i]]

for i in range(len(expression)):
    if expression[i].isdigit():
        stack.append(expression[i])
    else:
        result = 0
        one = float(stack.pop())
        two = float(stack.pop())
        if expression[i] == '*':
            result = one * two
        elif expression[i] == '+':
            result = one + two
        elif expression[i] == '-':
            result = two - one
        else:
            result = two / one

        stack.append(result)

print(format(stack[0], ".2f"))
