from sys import stdin

input = stdin.readline

word = list(input().strip())
word_list = []
n = len(word)

for i in range(n):
    tmpword = ''.join(word)
    word_list.append(tmpword)
    word.pop(0)

word_list.sort()
for w in word_list:
    print(w)
