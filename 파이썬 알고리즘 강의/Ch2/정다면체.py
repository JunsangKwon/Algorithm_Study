from sys import stdin

input = stdin.readline

total = [0] * 42
answer = []

n, m = map(int, input().split())

for i in range(1, n+1):
    for j in range(1, m+1):
        total[i+j] += 1

for i in range(len(total)):
    if(total[i] == max(total)):
        answer.append(i)

for a in answer:
    print(a, end=" ")
