def solution(balls, share):
    answer = 1
    for _ in range(share):
        answer = answer * balls
        balls -= 1
    for _ in range(share):
        answer = answer // share
        share -= 1
    return int(answer)