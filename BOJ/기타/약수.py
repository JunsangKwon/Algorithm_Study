from sys import stdin, stdout

input = stdin.readline


num = int(input())
divisors = list(map(int, input().split()))
divisors.sort()

print(divisors[0] * divisors[-1])
