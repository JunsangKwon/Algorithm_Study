from sys import stdin

t = int(input())
answer = []

for i in range(t):
    n = int(input())
    data = []
    for j in range(n):
        university_data = list(input().split())
        data.append(university_data)

    data.sort(key=lambda x: (-int(x[1]), x[0]))
    answer.append(data[0][0])

for a in answer:
    print(a)
