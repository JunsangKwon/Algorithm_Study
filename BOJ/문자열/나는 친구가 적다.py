from sys import stdin

input = stdin.readline

s = input().strip()
new_s = ''
k = input().strip()

for i in range(len(s)):
    if(ord(s[i]) >= 48 and ord(s[i]) <= 57):
        continue
    else:
        new_s += s[i]

if k in new_s:
    print(1)
else:
    print(0)
