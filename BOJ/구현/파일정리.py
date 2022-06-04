from collections import Counter

n = int(input())
extensions = []
answer = []

for i in range(n):
    files = input()
    dot_index = 0
    for j in range(len(files)):
        if files[j] == '.':
            dot_index = j
            break
    extensions.append(files[dot_index+1:])

answer = Counter(extensions).most_common()
answer.sort()

for i in range(len(answer)):
    for j in range(2):
        print(answer[i][j], end=" ")
    print()
