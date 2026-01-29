def solution(price, money, count):
    sum_price = 0
    for i in range(1, count + 1):
        sum_price += price * i
    answer = sum_price - money
    if answer < 0:
        answer = 0
    return answer