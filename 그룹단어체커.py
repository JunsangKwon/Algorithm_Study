n = int(input())
words = []
already = []
count = 0
flag = False
for i in range(n):
    word = input()
    words.append(word)

for i in range(n):
    tmp = '-'
    for j in range(len(words[i])):
        if(tmp == words[i][j]):
            continue
        else:
            already.append(words[i][j])
            tmp = words[i][j]

    for k in already:
        cnt = already.count(k)
        if cnt != 1:
            flag = True

    if not flag:
        count += 1

    flag = False
    already.clear()

print(count)
