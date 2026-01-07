def solution(order):
    answer = 0
    for coffee in order:
        if coffee.find("americano") != -1:
            answer += 4500
            continue
        elif coffee.find("cafelatte") != -1:
            answer += 5000
        elif coffee.find("anything") != -1:
            answer += 4500
    return answer