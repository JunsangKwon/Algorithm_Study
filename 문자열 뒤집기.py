s = input()
numlist = []
zero = 0
one = 0
for i in range(len(s)):
    numlist.append(int(s[i]))

prevalue = 2
for i in numlist:
    if(i == prevalue):
        continue
    elif(i != prevalue):
        prevalue = i
        if(i == 0):
            zero += 1
        elif(i == 1):
            one += 1

print(min(zero, one))
        
        
