student = [0] * 31

for i in range(28):
    student[int(input())] += 1

for i in range(1, 31):
    if student[i] != 1:
        print(i)
