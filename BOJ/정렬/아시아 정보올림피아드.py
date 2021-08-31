from sys import stdin

input = stdin.readline

records = []
n = int(input())

for i in range(n):
    record = list(map(int, input().split()))
    records.append(record)

records.sort()
