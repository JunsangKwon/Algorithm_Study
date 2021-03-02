n, m = map(int, input().split())
minimum = []

for i in range(n):
    array = list(map(int, input().split()))
    minimum.append(min(array))

print(max(minimum))
