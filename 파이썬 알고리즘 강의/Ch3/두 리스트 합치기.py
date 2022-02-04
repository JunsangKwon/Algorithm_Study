from sys import stdin

input = stdin.readline

n = int(input())
first_array = list(map(int, input().split()))
m = int(input())
second_array = list(map(int, input().split()))
final_array = first_array + second_array
final_array.sort()

for i in final_array:
    print(i, end=" ")
