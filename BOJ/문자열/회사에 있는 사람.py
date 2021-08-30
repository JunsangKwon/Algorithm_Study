from sys import stdin

input = stdin.readline

company_log = []
company = {}

n = int(input())

for i in range(n):
    company_log.append(list(input().strip().split()))

for i in range(n):
    if(company_log[i][1] == "enter"):
        company[company_log[i][0]] = 1
    else:
        del company[company_log[i][0]]

company_in = list(company.keys())
company_in.sort(reverse=True)

for i in range(len(company_in)):
    print(company_in[i])
