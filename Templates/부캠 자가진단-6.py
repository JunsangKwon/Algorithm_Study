arr = [1, 2, 3, 3, 3, 3, 4, 4]
repeatnum = [0]*101
answer = []
flag = False

for i in arr:
    repeatnum[i] += 1

for i in range(len(repeatnum)):
    if(repeatnum[i] <= 1):
        continue
    else:
        flag = True
        answer.append(repeatnum[i])

if(not flag):
    print([-1])
else:
    print(answer)
