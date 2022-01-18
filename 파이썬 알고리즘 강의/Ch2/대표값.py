from sys import stdin

input = stdin.readline

studentList = []

n = int(input())
score = list(map(int, input().split()))
avg = round(sum(score) / len(score))

for i in range(n):
    tmp = []
    tmp.append(abs(score[i] - avg))
    tmp.append(score[i] - avg)
    tmp.append(i+1)
    studentList.append(tmp)

studentList.sort(key=lambda x: (x[0], -x[1], x[2]))

print(avg, studentList[0][2])
