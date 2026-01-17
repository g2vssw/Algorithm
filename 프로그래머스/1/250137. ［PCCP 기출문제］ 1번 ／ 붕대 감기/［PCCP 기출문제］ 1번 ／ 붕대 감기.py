def solution(bandage, health, attacks):
    answer = health
    success = 0
    flag = 0
    for t in range(1, attacks[-1][0] + 1):
        for att in attacks:
            if att[0] > t:
                flag = 0
                break
            elif att[0] == t:
                flag = 1
                success = 0
                answer -= att[1]
                break
        if flag == 1:
            if answer <= 0:
                answer = -1
                break
            continue
        answer += bandage[1]
        success += 1
        if success == bandage[0]:
            answer += bandage[2]
            success = 0
        if answer > health:
            answer = health
    return answer