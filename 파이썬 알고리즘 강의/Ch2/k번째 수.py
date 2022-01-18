from sys import stdin

input = stdin.readline
T = int(input())
answer = []

for t in range(T):
    n, s, e, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers = numbers[s-1:e]
    numbers.sort()
    answer.append(numbers[k-1])

for a in answer:
    print(a)
