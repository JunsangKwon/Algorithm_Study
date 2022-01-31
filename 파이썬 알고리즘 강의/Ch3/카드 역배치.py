from sys import stdin

input = stdin.readline

cards = [str(i+1) for i in range(20)]
ranges = []

for i in range(10):
    r = list(map(int, input().split()))
    ranges.append(r)

for i in range(10):
    start = ranges[i][0] - 1
    end = ranges[i][1] - 1
    if start == 0:
        recards = cards[end::-1]
    else:
        recards = cards[end:(start-1):-1]
    index = 0
    for j in range(start, end+1):
        cards[j] = recards[index]
        index += 1

print(' '.join(cards))
