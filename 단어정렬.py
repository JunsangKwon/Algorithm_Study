n = int(input())
tuplelist = []

for i in range(n):
    tmplist = []
    tmpword = input()
    tmplen = len(tmpword)
    tmplist.append(tmplen)
    tmplist.append(tmpword)
    tuplelist.append(tuple(tmplist))

tuplelist.sort(key=lambda x: (x[0], x[1]))
tmp = " "

for (_, word) in tuplelist:
    if tmp == word:
        continue
    print(word)
    tmp = word
