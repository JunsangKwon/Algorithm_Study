import math

n = int(input())
num_list = []
flag = False


for i in range(n):
    num_list.append(i+1)

while True:
    if len(num_list) == 1:
        print(num_list[0])
        break
    for i in range(0, math.ceil(len(num_list)/2)):
        if len(num_list) == 1:
            break
        else:
            del num_list[i]
