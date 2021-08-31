from sys import stdin

input = stdin.readline

word = input().strip().split(':')

a = int(word[0])
b = int(word[1])

if(b > a):
    a, b = b, a

while(b != 0):
    a = a % b
    a, b = b, a

word[0] = str(int(word[0]) // a)
word[1] = str(int(word[1]) // a)

print(':'.join(word))
