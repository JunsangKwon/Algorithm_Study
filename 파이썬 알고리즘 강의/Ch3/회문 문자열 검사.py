from sys import stdin

input = stdin.readline

determine_list = []
words = []
n = int(input())
flag = False

for i in range(n):
    word = input().strip()
    words.append(word)

for i in range(len(words)):
    flag = False
    word_count = len(words[i])
    for j in range(word_count // 2):
        front_word = words[i][j].lower()
        back_word = words[i][-j-1].lower()
        if front_word != back_word:
            determine_list.append("NO")
            flag = True
            break
    if not flag:
        determine_list.append("YES")


for d in determine_list:
    print(d)
