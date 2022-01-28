from sys import stdin
import math

input = stdin.readline


def reverse(x):
    stringX = str(x)
    reversed_str = stringX[::-1]
    reversed_str = reversed_str.lstrip("0")  # 문자열 앞쪽 0들을 제거한다
    return int(reversed_str)


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


n = int(input())
nums = list(map(int, input().split()))
answer = []

for i in range(len(nums)):
    candindate_num = reverse(nums[i])
    determine = isPrime(candindate_num)
    if determine == True:
        answer.append(candindate_num)

for i in range(len(answer)):
    print(answer[i], end=" ")
