import sys

flagC = False
flagP = False
flagC2 = False
lastFlag = False

words = list(map(str, sys.stdin.readline().strip()))
for i in words:
    if(i == 'U'):
        flagC = True
    if(flagC):
        if(i == 'C'):
            flagP = True
            flagC = False
    if(flagP):
        if(i == 'P'):
            flagC2 = True
            flagP = False
    if(flagC2):
        if(i == 'C'):
            lastFlag = True
            flagC2 = False
            break

if(lastFlag):
    print("I love UCPC")
else:
    print("I hate UCPC")
