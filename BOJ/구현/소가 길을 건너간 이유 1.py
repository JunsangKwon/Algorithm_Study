cows = [-1] * 101
cows_count = [0] * 101

t = int(input())

for i in range(t):
    index, value = map(int, input().split())
    if cows[index] != -1 and cows[index] != value:
        cows_count[index] += 1

    cows[index] = value

print(sum(cows_count))
