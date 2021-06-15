x = input()
numlist = []
operlist = []

for i in range(len(x)):
    numlist.append(int(x[i]))

for i in numlist:
    if(i == 0 or i == 1):
        operlist.append("+")
    else:
        operlist.append("*")
operlist.pop()
result = numlist[0]

for i in range(len(operlist)):
    if(operlist[i] == "+"):
        result += numlist[i+1]
    elif(operlist[i] == "*"):
         result *= numlist[i+1]

print(result)
        
