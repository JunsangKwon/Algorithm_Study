from sys import stdin

input = stdin.readline

n, k = map(int, input().split())
cards = list(map(int, input().split()))
sums = []

for i in range(len(cards)):
    for j in range(i+1, len(cards)):
        for l in range(j+1, len(cards)):
            sums.append(cards[i]+cards[j]+cards[l])

sums = list(set(sums))
sums.sort(reverse=True)
print(sums[k-1])
