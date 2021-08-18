from sys import stdin, stdout

n = int(stdin.readline())
scores = []
for i in range(n):
    score = list(stdin.readline().split())
    scores.append(score)

scores.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n):
    print(scores[i][0])
