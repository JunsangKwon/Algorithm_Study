def findsum(value, count):
    i = 1
    while(value > 0):
        value -= i
        i += 1
        count += 1

    summ = (count)*(count+1)*(2*count + 1)//6
    summ -= (count) * abs(value)

    return summ


a, b = map(int, input().split())
bcopy = b
acopy = a-1

answer = findsum(bcopy, 0) - findsum(acopy, 0)
print(answer)
