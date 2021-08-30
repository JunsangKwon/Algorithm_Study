from sys import stdin

input = stdin.readline
original_words = []

n = int(input())
for i in range(n):
    word = input()
    original_words.append(word)

increasing_words = sorted(original_words)
decreasing_words = sorted(original_words, reverse=True)


if(original_words == increasing_words):
    print("INCREASING")
elif(original_words == decreasing_words):
    print("DECREASING")
else:
    print("NEITHER")
