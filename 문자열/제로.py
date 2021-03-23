# sol. 0을 stack의 pop이라고 생각해서 품

k = int(input())
money = []

for i in range(k):
    tmp = int(input())
    if(tmp != 0):
        money.append(tmp)
    else:
        money.pop()

print(sum(money))
