from sys import stdin

input = stdin.readline

n = int(input())
result = list(map(int, input().split()))
extra_point = 0
total_point = 0

for i in range(len(result)):
    if result[i] == 1:
        total_point += (1 + extra_point)
        extra_point += 1
    else:
        extra_point = 0

print(total_point)
