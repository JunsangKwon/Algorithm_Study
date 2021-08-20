from sys import stdin

n, m = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))

c = a + b

c.sort()

for i in c:
    print(i, end=" ")
