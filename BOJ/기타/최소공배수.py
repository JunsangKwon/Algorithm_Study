from sys import stdin

t = int(stdin.readline())
answer = []


def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


for i in range(t):
    a, b = map(int, stdin.readline().split())
    max_divisor = gcd(a, b)
    answer.append(max_divisor * (a // max_divisor) * (b // max_divisor))


for a in answer:
    print(a)
