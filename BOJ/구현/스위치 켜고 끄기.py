switch_num = int(input())
switches = list(map(int, input().split()))
n = int(input())

for i in range(n):
    gender, num = map(int, input().split())
    left_index = num-2
    right_index = num
    num_total = num

    if gender == 1:
        while num_total <= switch_num:
            if switches[num_total-1] == 0:
                switches[num_total-1] = 1
            else:
                switches[num_total-1] = 0

            num_total += num
    elif gender == 2:
        if switches[num-1] == 0:
            switches[num-1] = 1
        else:
            switches[num-1] = 0

        while left_index >= 0 and right_index < switch_num and switches[left_index] == switches[right_index]:
            if switches[left_index] == 0:
                switches[left_index] = 1
                switches[right_index] = 1
            else:
                switches[left_index] = 0
                switches[right_index] = 0

            left_index -= 1
            right_index += 1


for i in range(switch_num):
    print(switches[i], end=" ")
    if (i+1) % 20 == 0:
        print()
