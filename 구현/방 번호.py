import sys

roomnum = sys.stdin.readline().strip()
numlist = []
for num in roomnum:
    numlist.append(int(num))

frequency = [0]*10

for num in numlist:
    frequency[num] += 1

if(max(frequency) == frequency[6] or max(frequency) == frequency[9]):
    if((frequency[6] + frequency[9]) % 2 == 0):
        frequency[6] = (frequency[6] + frequency[9])//2
        frequency[9] = frequency[6]
    else:
        frequency[6] = (frequency[6] + frequency[9])//2 + 1
        frequency[9] = frequency[6]

print(max(frequency))
