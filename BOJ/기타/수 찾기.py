from sys import stdin, stdout

input = stdin.readline


def binary_search(array, target, start, end):
    while(start <= end):
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid + 1
    return 0


answer = []
n = int(input())
a_list = list(map(int, input().split()))
a_list.sort()
m = int(input())
b_list = list(map(int, input().split()))

for i in range(m):
    target = b_list[i]
    answer.append(binary_search(a_list, target, 0, n-1))

for a in answer:
    print(a)
