T = int(input())
answer = []

for t in range(T):
    n = int(input())
    num_list = list(map(int, input().split()))
    answer.append(((min(num_list)), max(num_list)))

for i in range(len(answer)):
    print(answer[i][0], answer[i][1])
