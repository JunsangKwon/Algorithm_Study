from sys import stdin

dokam = {}
answer = []
input = stdin.readline

n, m = map(int, input().split())
for i in range(n):
    poketmon = input().strip()
    dokam[poketmon] = '%d' % (i+1)
    dokam[str(i+1)] = poketmon

for i in range(m):
    question = input().strip()
    answer.append(dokam[question])

for i in answer:
    print(i)
