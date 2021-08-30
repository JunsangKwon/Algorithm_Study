from sys import stdin

input = stdin.readline

n = int(input())
candidate_code = list(map(int, input().split()))
normal_word = input().strip()
real_code = []

for i in range(len(normal_word)):
    if(ord(normal_word[i]) >= 65 and ord(normal_word[i]) <= 90):
        real_code.append(ord(normal_word[i])-64)
    elif(ord(normal_word[i]) >= 97 and ord(normal_word[i]) <= 122):
        real_code.append(ord(normal_word[i])-70)
    elif(ord(normal_word[i]) == 32):
        real_code.append(0)
    else:
        continue

candidate_code.sort()
real_code.sort()

if(candidate_code == real_code):
    print("y")
else:
    print("n")
