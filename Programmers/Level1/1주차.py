def solution(price, money, count):
    totalPrice = 0
    for i in range(1, count+1):
        totalPrice += price * i

    return totalPrice - money if totalPrice > money else 0
