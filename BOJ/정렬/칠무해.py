from sys import stdin

input = stdin.readline

n = int(input())
scores = []

for i in range(n):
    scores.append(float(input()))

scores.sort()

for i in range(7):
    print('%.3f' % scores[i])
