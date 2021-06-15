# Sol1. 두 개의 list를 이어서 중복 값을 set에 넣었다가 다시 list로 넣어 정렬하는 방식 (X) -> 시간 초과
# Sol2. 두 개의 set으로 교집합 연산을 하여 그걸 list에 넣어 정렬하는 방식
nohear = set()
nosee = set()
count = 0
repeat = []

n, m = map(int, input().split())

for i in range(n):
    name = input()
    nohear.add(name)

for j in range(m):
    name = input()
    nosee.add(name)

nohearandsee = nohear & nosee       # Set의 교집합 연산 => &, 합집합 연산 => |

print(len(nohearandsee))

for k in nohearandsee:
    repeat.append(k)

repeat.sort()
for i in repeat:
    print(i)
