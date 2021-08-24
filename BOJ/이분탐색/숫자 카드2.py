from sys import stdin, stdout
from collections import Counter

input = stdin.readline


def binary_search_and_count(array, target, prequency, start, end):
    while(start <= end):
        mid = (start + end) // 2
        if array[mid] == target:
            return prequency[target]
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid + 1
    return 0


answer = []
n = int(input())
card_num = list(map(int, input().split()))
card_prequncy = Counter(card_num)
card_num.sort()

m = int(input())
check_num = list(map(int, input().split()))

for i in range(m):
    target = check_num[i]
    answer.append(binary_search_and_count(
        card_num, target, card_prequncy, 0, n))

for a in answer:
    print(a, end=' ')
