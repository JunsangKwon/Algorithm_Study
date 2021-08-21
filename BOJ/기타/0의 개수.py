from sys import stdin

answer = []
t = int(stdin.readline())
for i in range(t):
    zero_count = 0
    n, m = map(int, stdin.readline().split())
    for i in range(n, m+1):
        if '0' in str(i):
            zero_count += str(i).count('0')

    answer.append(zero_count)

for a in answer:
    print(a)
