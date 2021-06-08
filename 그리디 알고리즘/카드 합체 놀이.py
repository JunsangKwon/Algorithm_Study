n, m = map(int, input().split())

cards = list(map(int, input().split()))
answer = 0

for _ in range(m):
    cards.sort()
    newValue = cards[0] + cards[1]
    cards[0] = newValue
    cards[1] = newValue

for i in cards:
    answer += i

print(answer)
