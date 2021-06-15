import sys

seed = int(sys.stdin.readline().strip())
seeds = list(map(int, input().split()))

seedscopy = sorted(seeds, reverse=True)

for i in range(len(seedscopy)):
    seedscopy[i] += i

seedscopy = sorted(seedscopy, reverse=True)

print(seedscopy[0]+2)
