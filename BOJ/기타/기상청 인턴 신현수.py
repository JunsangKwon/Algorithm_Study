from sys import stdin

n, k = map(int, stdin.readline().split())

weather = list(map(int, stdin.readline().split()))
sum_of_weather_list = []

for i in range(n-k+1):
    sum_of_weather = 0
    for j in range(i, i+k):
        sum_of_weather += weather[j]
    sum_of_weather_list.append(sum_of_weather)

print(max(sum_of_weather_list))
