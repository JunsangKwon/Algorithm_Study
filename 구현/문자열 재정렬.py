s = input()
newlist1 = []
sumofnum = 0

for i in s:
    if(ord(i)>64):
        newlist1.append(ord(i))
    else:
        sumofnum += int(i)

newlist1.sort()

for i in newlist1:
    print(chr(i), end='')
    
print(sumofnum)
    
    

