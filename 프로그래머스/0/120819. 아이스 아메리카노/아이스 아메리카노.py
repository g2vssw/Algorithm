def solution(money):
    answer = []
    coffee = money // 5500
    coin = money % 5500
    answer.append(coffee)
    answer.append(coin)
    return answer