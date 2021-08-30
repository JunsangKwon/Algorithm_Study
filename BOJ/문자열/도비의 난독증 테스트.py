from sys import stdin

input = stdin.readline
answer = []

while True:
    words = []
    n = int(input())
    if n == 0:
        break

    for i in range(n):
        word = input().strip()
        words.append([word, word.lower()])

    words.sort(key=lambda x: (x[1], x[0]))

    answer.append(words[0][0])

for a in answer:
    print(a)
