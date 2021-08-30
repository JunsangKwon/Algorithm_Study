from sys import stdin, stdout

input = stdin.readline

n, d = map(int, input().split())
d = str(d)
prequency = 0

for i in range(1, n+1):
    i = str(i)
    prequency += i.count(d)

print(prequency)
