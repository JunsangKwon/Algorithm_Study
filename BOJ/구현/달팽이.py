n = int(input())
target = int(input())
snail = [[0] * n for _ in range(n)]
uri = [-1, 0]
urj = [0, 1]
dli = [1, 0]
dlj = [0, -1]
movei = []
movej = []
count = 0
level = 1
si = n // 2
sj = n // 2
answeri = 0
answerj = 0

while count <= n**2:
    if level % 2 == 0:
        for i in range(level):
            movei.append(dli[0])
            movej.append(dlj[0])
            count += 1

        for i in range(level):
            movei.append(dli[1])
            movej.append(dlj[1])
            count += 1

        level += 1

    else:
        for i in range(level):
            movei.append(uri[0])
            movej.append(urj[0])
            count += 1

        for i in range(level):
            movei.append(uri[1])
            movej.append(urj[1])
            count += 1

        level += 1


for i in range(n ** 2):
    if target == i+1:
        answeri = si + 1
        answerj = sj + 1
    snail[si][sj] = i + 1
    si = si + movei[i]
    sj = sj + movej[i]

for i in range(n):
    for j in range(n):
        print(snail[i][j], end=" ")
    print()

print(answeri, answerj)
