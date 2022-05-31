n = int(input())
words = []
count = 0

for i in range(n):
    word = input()
    new_word = word[0]
    prev = word[0]
    for j in range(1, len(word)):
        if prev == word[j]:
            continue
        else:
            new_word += word[j]
            prev = word[j]

    words.append(new_word)

for word in words:
    if len(word) == len(set(word)):
        count += 1

print(count)
