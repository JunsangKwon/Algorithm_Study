# sol. 문자열 -> 숫자 -> 내림차순 정렬 -> 문자열
numstr = input()
numlist = []
for i in numstr:
    numlist.append(int(i))

numlist.sort()
numlist.reverse()
numstr = ''

for i in numlist:
    numstr += str(i)

print(numstr)
