from sys import stdin

input = stdin.readline

answers = []
boxes = []
t = int(input())

for i in range(t):
    count = 0
    candy_num, box_num = map(int, input().split())
    for j in range(box_num):
        width, height = map(int, input().split())
        boxes.append(width*height)

    boxes.sort(reverse=True)

    for j in range(len(boxes)):
        candy_num -= boxes[j]
        count += 1
        if(candy_num <= 0):
            answers.append(count)
            boxes.clear()
            break

for answer in answers:
    print(answer)
