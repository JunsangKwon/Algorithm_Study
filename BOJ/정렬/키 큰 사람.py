from sys import stdin

input = stdin.readline

height_list = []
heights = []
answer = []
answers = []

while True:
    n = int(input())
    if(n == 0):
        break
    for i in range(n):
        height = list(input().split())
        height[1] = float(height[1])
        heights.append(height[1])
        height_list.append(height)

    max_height = max(heights)

    for i in range(len(height_list)):
        if(height_list[i][1] == max_height):
            print(height_list[i][0], end=' ')

    height_list.clear()
    heights.clear()
    print()
