from sys import stdin

input = stdin.readline

n = int(input())

num_list = list(map(int, input().split()))

num_list.sort()

for num in num_list:
    print(num, end=" ")
