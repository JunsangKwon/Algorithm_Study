n = int(input())

# sol1
'''
for i in range(n):
    a_binary, b_binary = map(str, input().split())
    a_binary = '0b' + a_binary
    b_binary = '0b' + b_binary
    a = int(a_binary, 2)
    b = int(b_binary, 2)
    ans_binary = bin(a+b)

    print(ans_binary[2:])
'''

# sol2


def change(x):
    binary = ''
    if x == 0:
        binary = '0'

    while x > 0:
        div = x // 2
        mod = x % 2
        x = div
        binary += str(mod)

    return binary[::-1]


for i in range(n):
    a_binary, b_binary = map(str, input().split())
    a = int(a_binary, 2)
    b = int(b_binary, 2)

    print(change(a+b))
