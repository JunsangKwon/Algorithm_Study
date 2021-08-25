from sys import stdin, stdout

input = stdin.readline


m, n = map(int, input().split())
snacks = list(map(int, input().split()))
start = 1
end = max(snacks)
result = 0
snack_num = 0

while(start <= end):
    sum_of_snack = 0
    length = (start + end) // 2
    for i in range(len(snacks)):
        sum_of_snack += (snacks[i] // length)

    if sum_of_snack < m:
        end = length - 1
    else:
        result = length
        start = length + 1

print(result)
