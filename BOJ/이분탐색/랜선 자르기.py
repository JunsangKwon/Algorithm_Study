from sys import stdin, stdout

input = stdin.readline

k, n = map(int, input().split())
lanterns = []

for i in range(k):
    lantern = int(input())
    lanterns.append(lantern)

start = 1
end = max(lanterns)
result = 0

while(start <= end):
    sum_of_lantern = 0
    length = (start + end) // 2
    for i in range(len(lanterns)):
        sum_of_lantern += (lanterns[i] // length)

    if sum_of_lantern < n:
        end = length - 1
    else:
        result = length
        start = length + 1

print(result)
