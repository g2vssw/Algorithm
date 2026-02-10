def solution(name, yearning, photo):
    answer = []
    longing_score_dict = {}
    for i in range(len(name)):
        longing_score_dict[name[i]] = yearning[i]
    for pic in photo:
        value = 0
        for person in pic:
            if person in longing_score_dict:
                value += longing_score_dict[person]
        answer.append(value)
    return answer