from sys import stdin

input = stdin.readline

word = input().strip()
bomb = input().strip()
bomb_num = len(bomb)
stack = []

for i in range(len(word)):
    stack.append(word[i])
    if word[i] == bomb[-1] and bomb == "".join(stack[-bomb_num:]):
        del stack[-bomb_num:]

if len(stack) == 0:
    print("FRULA")
else:
    print(''.join(stack))
