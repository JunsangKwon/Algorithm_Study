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
t = int(input())

for i in range(t):
    n = int(input())
    note1 = list(map(int, input().split()))
    note1.sort()
    m = int(input())
    note2 = list(map(int, input().split()))

    for j in range(m):
        target = note2[j]
        answer.append(binary_search(note1, target, 0, n-1))


for a in answer:
    print(a)
