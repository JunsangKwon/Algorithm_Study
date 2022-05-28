from sys import stdin

input = stdin.readline

number = input().strip()
ten_number = int('0o' + number, 8)
answer = bin(ten_number)
print(answer[2:])
