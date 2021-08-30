from sys import stdin

input = stdin.readline

t = int(input())
words = []
answer = []

for i in range(t):
    n = int(input())
    for j in range(n):
        word = input().strip()
        words.append(word)

    breaker = False
    for j in range(n):
        for k in range(n):
            if(j == k):
                continue
            candidate_word = words[j] + words[k]
            if(candidate_word == candidate_word[::-1]):
                answer.append(candidate_word)
                breaker = True
                break
            else:
                continue
        if(breaker):
            break

    if(not breaker):
        answer.append(0)

    words.clear()

for a in answer:
    print(a)
