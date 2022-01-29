from sys import stdin

input = stdin.readline

filtered_words = []
word = input().strip()
divisor_count = 0

for i in range(len(word)):
    ascii_num = ord(word[i])
    if ascii_num >= 48 and ascii_num <= 57:
        filtered_words.append(word[i])

nums = int(''.join(filtered_words))

for i in range(1, nums+1):
    if nums % i == 0:
        divisor_count += 1

print(nums)
print(divisor_count)
