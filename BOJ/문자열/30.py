from sys import stdin

number_str_list = list(input())
number_str_list.sort(reverse=True)
num_list = []

for i in number_str_list:
    num_list.append(int(i))

if (num_list.count(0) == 0) or (sum(num_list) % 3 != 0):
    print(-1)
else:
    print(''.join(number_str_list))
