from sys import stdin

input = stdin.readline

n = int(input())
rewards = []

for i in range(n):
    a, b, c = map(int, input().split())
    if a == b and b == c:
        rewards.append(10000 + (a*1000))
    elif a == b or b == c or a == c:
        if b == c:
            rewards.append(1000 + (b * 100))
        else:
            rewards.append(1000 + (a * 100))
    else:
        rewards.append(max(a, b, c) * 100)

print(max(rewards))
