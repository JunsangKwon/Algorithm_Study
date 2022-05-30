money = int(input())
stock = list(map(int, input().split()))
bnp_money = money
timing_money = money
bnp_stocks = 0
timing_stocks = 0
bnp_total = 0
timing_total = 0
previous_value = stock[0]
down_stack = 0
up_stack = 0

for i in range(len(stock)):
    if bnp_money // stock[i] >= 1:
        bnp_stocks += bnp_money // stock[i]
        bnp_money = bnp_money % stock[i]

bnp_total = bnp_stocks * stock[-1] + bnp_money

for i in range(len(stock)):
    if previous_value < stock[i]:
        if down_stack != 0:
            down_stack = 0
        up_stack += 1
        previous_value = stock[i]
        if up_stack >= 3:
            if timing_stocks != 0:
                timing_total += timing_stocks * stock[i]
                timing_stocks = 0
    elif previous_value > stock[i]:
        if up_stack != 0:
            up_stack = 0
        down_stack += 1
        previous_value = stock[i]
        if down_stack >= 3:
            if timing_money // stock[i] >= 1:
                timing_stocks += timing_money // stock[i]
                timing_money = timing_money % stock[i]
    else:
        up_stack = 0
        down_stack = 0

if timing_stocks != 0:
    timing_total += timing_stocks * stock[-1] + timing_money
else:
    timing_total += timing_money

print(bnp_total)
print(timing_total)

if bnp_total > timing_total:
    print("BNP")
elif bnp_total < timing_total:
    print("TIMING")
else:
    print("SAMESAME")
