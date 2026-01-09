def solution(price):
    if price < 100000:
        answer = price
    elif 100000 <= price < 300000:
        answer = int(price * (95/100))
    elif 300000 <= price < 500000:
        answer = int(price * (90/100))
    else:
        answer = int(price * (80/100))
    return answer