coin = [500, 100, 50, 10]
x = int(input())
num = 0
for i in coin:
    num += x//i
    x = x% i

print(num)
    
    
