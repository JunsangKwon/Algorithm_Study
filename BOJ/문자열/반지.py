from sys import stdin

ring_list = []
word = input()
n = int(stdin.readline())
count = 0

for i in range(n):
    ring_word = input()
    ring_list.append(ring_word + ring_word)

for i in range(n):
    if word in ring_list[i]:
        count += 1

print(count)
