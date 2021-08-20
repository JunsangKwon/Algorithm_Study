from sys import stdin

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
nums = list(set(nums))
nums.sort()

for n in nums:
    print(n, end=' ')
